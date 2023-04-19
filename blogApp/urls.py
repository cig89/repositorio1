from django.urls import path
from blogApp import views

urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera.
    
    path("", views.blog, name ="Blog"),
    path("categoria/<nombreCategoria>/", views.FiltroCategoria, name ="FiltroCategoria"),
]