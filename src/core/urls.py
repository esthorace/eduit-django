from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="home"),
]

# Viejo
# urlpatterns = [
#     path("", views.index, name="home"),
#     path("saludar/", views.saludar),
#     path("saludar-tag/", views.saludar_tag),
#     path("parametros/<str:nombre>/<str:apellido>/", views.parametros_ruta),
#     path("ejercicio1/", views.ejercicio1),
#     path("notas/", views.ver_notas, name="notas"),
#     path("ejercicio2/", views.ejercicio2, name="ejercicio2"),
# ]
