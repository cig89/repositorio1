from django.shortcuts import render, HttpResponse


def home(request):  
    return render(request, "proyectoWebApp\home.html")

def blog(request):
    return render(request, "proyectoWebApp\blog.html")


def servicios(request):
    return render(request, "proyectoWebApp\servicios.html")

def contacto(request):
    return render(request, "proyectoWebApp\contacto.html")

def shop(request):
    return render(request, "proyectoWebApp\shop.html")

