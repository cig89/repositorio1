
from django.shortcuts import render
from .models import Producto

def shop(request):
    lista_productos = Producto.objects.all() # Devuelve un queryset(una lista de objetos)
    return render(request, "shop.html",{"lista_productos": lista_productos})
