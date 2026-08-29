from django.db import models
from django.db.models import constraints


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, default="", verbose_name="descripción")

    class Meta:
        verbose_name = "Categoría de Productos"
        verbose_name_plural = "Categorías de Productos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="categoría",
        related_name="productos",
    )
    nombre = models.CharField(max_length=100, db_index=True)
    descripcion = models.TextField(blank=True, default="", verbose_name="descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(
                fields=["categoria", "nombre"], name="unique_producto_categoria"
            )
        ]

    def __str__(self):
        if self.categoria:
            return f"{self.categoria} - {self.nombre}"
        return self.nombre
