from django.urls import path

from loginApp import views
#from .views import VistaRegistro


urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera.

    path("", views.get, name ="FormularioRegistro"),
    path("login/", views.iniciar_sesion, name ="Login"),
    path("logout/", views.cerrar_sesion, name ="Logout"),
    
]