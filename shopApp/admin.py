from django.contrib import admin

from shopApp.models import CategoriaProd,Producto

""" PARA CATEGORIA"""
#La clase creada a continuación es opcinal, simplemene nos permite personalizar como se ve la tabla y porque cambos buscar y filtrar
class CategoriaProdAdmin(admin.ModelAdmin):
    list_display  =  ['nombre','created', 'updated']  # esto son los campos que mostrará la tabla en el panel de administracion
    search_fields =  ['nombre','created', 'updated']  # esto son los campos para buscar la información
    list_filter   =  ['nombre']                       # son los filtros que aparecen 
    
    
admin.site.register(CategoriaProd, CategoriaProdAdmin)    #esto es obligatorio, ya que añade la tabla al panel de administración


""" PARA PRODUCTO"""
#La clase creada a continuación es opcinal, simplemene nos permite personalizar como se ve la tabla y porque cambos buscar y filtrar
class ProductoAdmin(admin.ModelAdmin):
    list_display  =  ['nombre', 'precio', 'disponibilidad', 'created','updated']        # esto son los campos que mostrará la tabla en el panel de administracion
    search_fields =  ['nombre', 'precio', 'disponibilidad','created', 'updated']        # esto son los campos para buscar la información
    list_filter   =  ['nombre']                                           # son los filtros que aparecen 
    
    
admin.site.register(Producto, ProductoAdmin)    #esto es obligatorio, ya que añade la tabla al panel de administración
