from django.urls import path
from carroApp import views

app_name = "Carro"

urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera.
    
    path("agregar/<int:producto_id>",  views.agregar_producto_vista,          name ="Agregar"),
    path("restar/<int:producto_id>",   views.restar_producto_vista,           name ="Restar"),
    path("eliminar/<int:producto_id>", views.eliminar_producto_vista,         name ="Eliminar"),
    path("limpiar/",                   views.eliminar_todos_productos_vista,  name ="Limpiar"),
    
    
]