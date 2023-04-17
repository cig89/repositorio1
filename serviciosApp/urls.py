from django.urls import path
from serviciosApp import views

urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera para ser utilizada en otro sitio.
    
    path("", views.servicios, name ="Servicios"),
]