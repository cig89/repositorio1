
from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto,CategoriaProd

def shop(request):
    lista_productos = Producto.objects.all() # Devuelve un queryset(una lista de objetos)
    lista_categorias = CategoriaProd.objects.all() #Devuelve un queryset con  todas las categorias
    return render(request, "shopApp/shop.html",{"lista_productos": lista_productos, "lista_categorias": lista_categorias})


#creo una vista para traer los productos filtrados por la categoria elegida por el usuario
def FiltroCategoriaShop(request,nombreCategoriaShop):
    ob_categoria = CategoriaProd.objects.filter(nombre = nombreCategoriaShop).first()
    if ob_categoria ==None:
        return HttpResponse(f"la categoria introducida: '{nombreCategoriaShop}' no existe")
    
    lista_productos_filtrados = Producto.objects.filter(categorias =ob_categoria).all() #se obtiene una lista de objetos(productos) de esa categoria
    if lista_productos_filtrados ==None or lista_productos_filtrados ==[]:
        return HttpResponse(f"No existen productos para la categoria '{ob_categoria}")
    
    return render(request, "shopApp/filtrarPorCategoriaShop.html", {"ob_categoria":ob_categoria,"lista_productos_filtrados": lista_productos_filtrados})


#Creo una vista para mostrar la descripción de cada producto
def DescripcionProducto(request,nombreProductoShop):
    ob_producto = Producto.objects.filter(nombre =nombreProductoShop).first()  #Devuele el objeto con el nombre que le llega a la función
    return render(request, "shopApp/descripcionProducto.html", {"ob_producto":ob_producto})


    