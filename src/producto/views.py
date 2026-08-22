from django.http import HttpRequest
from django.shortcuts import redirect, render

from producto.forms import CategoriaForm
from producto.models import Categoria


def index(request):
    categorias = Categoria.objects.all()
    return render(request, "producto/index.html", context={"categorias": categorias})


def categoria_create(request: HttpRequest):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = CategoriaForm()
    return render(request, "producto/categoria_form.html", {"form": form})
