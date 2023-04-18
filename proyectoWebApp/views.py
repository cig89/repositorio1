from unittest import loader
from django.shortcuts import render, HttpResponse


def home(request):  
    return render(request, "home.html")

def contacto(request):
    return render(request, "contacto.html")

def shop(request):
    return render(request, "shop.html")

def blog(request):
    context = locals()
    template ="blog.html"
    return render(request, template, context)  #mirar si cambiamos el dir en setting.py

