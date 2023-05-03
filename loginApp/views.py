from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import UserCreationForm

def autentication(request):
    return render(request, "loginApp/registro.html")


class VistaRegistro(View):
    def get(self, request): #Se crea el metodo get para mostrar el formulario
        form = UserCreationForm()  #se crea el formulario usando la clase que proporciona Django
        return render (request, "loginApp/registro.html", {"form":form})

    def post(self, request):
        pass
    