from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    #Abajo se enlazan los archivos url de cada aplicacion. 1er arg se pone la palabra para la url. El 2 arg es el archivo url de la app a enlazar.
    path("", include("proyectoWebApp.urls")), 
    
]
