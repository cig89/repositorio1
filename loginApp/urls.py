from django.urls import path
from .views import VistaRegistro

urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera.
    
    path("", VistaRegistro.as_view(), name ="Autenticacion"),
]