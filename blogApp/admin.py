from django.contrib import admin

from blogApp.models import Categoria, Post

""" PARA CATEGORIA"""
#La clase creada a continuación es opcinal, simplemene nos permite personalizar como se ve la tabla y porque cambos buscar y filtrar
class CategoriaAdmin(admin.ModelAdmin):
    list_display  =  ['nombre','created', 'updated']  # esto son los campos que mostrará la tabla en el panel de administracion
    search_fields =  ['nombre','created', 'updated']  # esto son los campos para buscar la información
    list_filter   =  ['nombre']                       # son los filtros que aparecen 
    
    
admin.site.register(Categoria, CategoriaAdmin)    #esto es obligatorio, ya que añade la tabla al panel de administración


""" PARA POST"""
#La clase creada a continuación es opcinal, simplemene nos permite personalizar como se ve la tabla y porque cambos buscar y filtrar
class PostAdmin(admin.ModelAdmin):
    list_display  =  ['titulo', 'contenido', 'autor','created', 'updated']        # esto son los campos que mostrará la tabla en el panel de administracion
    search_fields =  ['titulo', 'contenido', 'autor','created', 'updated']        # esto son los campos para buscar la información
    list_filter   =  ['titulo','autor']                                           # son los filtros que aparecen 
    
    
admin.site.register(Post, PostAdmin)    #esto es obligatorio, ya que añade la tabla al panel de administración