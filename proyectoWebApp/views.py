from unittest import loader
from django.shortcuts import render, HttpResponse


def home(request):  
    return render(request, "home.html")



def shop(request):
    return render(request, "shop.html")



