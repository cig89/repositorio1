from django.urls import path
from contactoApp import views

urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera.
    
    path("", views.contacto, name ="Contacto"),
]