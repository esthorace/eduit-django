from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from producto.forms import CategoriaForm
from producto.models import Categoria


def categoria_list(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    return render(request, "producto/categoria_list.html", context={"categorias": categorias})


def categoria_create(request: HttpRequest) -> HttpResponse:
    form = CategoriaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "La categoría fue creada exitosamente")
        return redirect("producto:categoria_list")

    return render(request, "producto/categoria_form.html", {"form": form})


def categoria_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Categoria, id=pk)
    form = CategoriaForm(request.POST or None, instance=query)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "La categoría fue actualizada")
        return redirect("producto:categoria_list")

    return render(request, "producto/categoria_form.html", {"form": form})


def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    categoria = get_object_or_404(Categoria, id=pk)
    return render(request, "producto/categoria_detail.html", {"categoria": categoria})


def categoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    categoria = get_object_or_404(Categoria, id=pk)
    if request.method == "POST":
        categoria.delete()
        messages.success(request, "La categoría fue eliminada")
        return redirect("producto:categoria_list")
    return render(request, "producto/categoria_confirm_delete.html", {"categoria": categoria})
