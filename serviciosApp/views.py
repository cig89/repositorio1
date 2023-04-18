from django.shortcuts import render

from .models import Servicio  #importamos la vista

def servicios(request):
    lista_servicios =Servicio.objects.all() #obtenemos un queryset, es decir, una lista con objetos. los objetos son los registros de la BBDD
    return render(request, "servicios.html", {"lista_servicios": lista_servicios})  #le pasamos el segundo argumento que es lo que enviamos al template

