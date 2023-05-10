
from django.shortcuts import render

from carroApp.views import Carro


def home(request):  
    return render(request, "home.html")







