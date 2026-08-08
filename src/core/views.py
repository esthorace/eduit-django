from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    return HttpResponse("Hola desde Django")


def saludar_tag(request):
    app = "Django"
    mensaje = f"<h1>Este es el título de mi <i>{app}</i></h1>"
    print(mensaje)
    return HttpResponse(mensaje)


def parametros_ruta(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")


def index(request):
    from datetime import datetime

    año_actual = datetime.now().year
    contexto = {"año": año_actual, "autor": "EduIT"}
    return render(request, "core/index.html", contexto)


def ejercicio1(request):
    nombre = "Louis"
    apellido = "Beethoven"
    context = {"nombre": nombre, "apellido": apellido}
    return render(request, "core/ejercicio1.html", context)


def ver_notas(request):
    lista_notas = [10, 7, 4, 7, 8, 3, 5, 6]
    return render(request, "core/notas.html", {"notas": lista_notas})


def ejercicio2(request):
    usuarios = [
        {"nombre": "juan", "email": "juan@django"},
        {"nombre": "santi", "email": "juan@django"},
        {"nombre": "agustín", "email": "juan@django"},
    ]
    return render(request, "core/ejercicio2.html", {"usuarios": usuarios})
