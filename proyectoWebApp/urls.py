from django.urls import path
from proyectoWebApp import views

urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera para ser utilizada en otro sitio.

    path("home/",      views.home,      name ="Home"), 
    path("shop/",      views.shop,      name ="Shop"),
    path("servicios/", views.servicios, name ="Servicios"),
    path("contacto/",  views.contacto,  name ="Contacto"),
    path("blog/",      views.blog,      name ="Blog"),
]