from unittest import loader
from django.shortcuts import render, HttpResponse


def home(request):  
    return render(request, "home.html")

def contacto(request):
    return render(request, "contacto.html")

def shop(request):
    return render(request, "shop.html")



