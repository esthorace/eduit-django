from django.shortcuts import render

from producto.models import Categoria


def index(request):
    categorias = Categoria.objects.all()
    return render(request, "producto/index.html", context={"categorias": categorias})
