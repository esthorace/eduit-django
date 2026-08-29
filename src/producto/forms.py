from django import forms

from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("nombre",)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("categoria", "nombre", "descripcion", "precio", "stock")

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo")
        return stock
