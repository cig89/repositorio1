
from django.urls import path
from proyectoWebApp import views

from django.conf import settings
from django.conf.urls.static  import static


urlpatterns = [
    #el 1er arg es la palabra para la url. El 2arg es la ruta a la view. El 3arg es el nombre que le damos a la ruta entera para ser utilizada en otro sitio.
    path("",      views.home,      name ="Home")
]

#a las url de arriba les agregamos lo siguiente
urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



