from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from producto.forms import ProductoForm
from producto.models import Producto


class ProductoListView(ListView):
    model = Producto


class ProductoDetailView(DetailView):
    model = Producto


class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")
    success_message = "El producto se ha creado exitosamente"


class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")
    success_message = "El producto se ha actualizado exitosamente"


class ProductoDeleteView(SuccessMessageMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("producto:producto_list")
    success_message = "El producto se ha eliminado exitosamente"
