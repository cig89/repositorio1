
from django.urls import path
from shopApp import views


urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera para ser utilizada en otro sitio.
    path("",      views.shop,      name ="Shop"),
    path("categoria/<nombreCategoriaShop>", views.FiltroCategoriaShop, name ="FiltroCategoriaShop"),
    path("descripcion/<nombreProductoShop>", views.DescripcionProducto, name ="DescripcionProductoShop")

]