from django import forms

from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("nombre",)
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. Tecnología"}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("categoria", "nombre", "descripcion", "precio", "stock")
        widgets = {
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del producto"}),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Describe el producto", "rows": 4}
            ),
            "precio": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "0.00", "step": "0.01", "min": "0"}
            ),
            "stock": forms.NumberInput(attrs={"class": "form-control", "placeholder": "0", "min": "0"}),
        }

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
