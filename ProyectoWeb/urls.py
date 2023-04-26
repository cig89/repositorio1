from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    #Abajo se enlazan los archivos url de cada aplicacion. 1er arg se pone la palabra para la url. El 2 arg es el archivo url de la app a enlazar.
    path("",           include("proyectoWebApp.urls")), 
    path("servicios/", include("serviciosApp.urls")),
    path("blog/",      include("blogApp.urls")),
    path("contacto/",  include("contactoApp.urls")),
    path("shop/",      include("shopApp.urls")),
    path("carro/",     include("carroApp.urls")),
    
]

