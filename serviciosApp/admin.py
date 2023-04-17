from django.contrib import admin
from .models import Servicio

#La clase creada a continuación es opcinal, simplemene nos permite personalizar como se ve la tabla y porque cambos buscar y filtrar
class ServicioAdmin(admin.ModelAdmin):
    list_display  =  ['titulo', 'contenido', 'imagen','created', 'updated']  # esto son los campos que mostrará la tabla en el panel de administracion
    search_fields =  ['titulo', 'contenido','created', 'updated']             # esto son los campos para buscar la información
    list_filter   =  ['titulo', 'contenido']                                  #son los filtros que aparecen 
    
    
admin.site.register(Servicio, ServicioAdmin)    #esto es obligatorio, ya que añade la tabla al panel de administración