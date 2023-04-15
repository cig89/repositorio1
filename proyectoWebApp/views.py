from unittest import loader
from django.shortcuts import render, HttpResponse


def home(request):  
    return render(request, "proyectoWebApp\home.html")

def servicios(request):
    return render(request, "proyectoWebApp\servicios.html")

def contacto(request):
    return render(request, "proyectoWebApp\contacto.html")

def shop(request):
    return render(request, "proyectoWebApp\shop.html")

# def blog(request):
#     return render(request, ' proyectoWebApp\blog.html ')  #si no lo carga cuando se cree la app, probar con otra forma

def blog(request):
    t1 = loader.get_template(" proyectoWebApp/blog.html")
    documento = t1.render({})
    return HttpResponse(documento)