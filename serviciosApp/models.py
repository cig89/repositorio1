from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    """se crean los campos created & updated para filtrar en la tabla"""
    created = models.DateTimeField(auto_now_add =True) #agrega la fecha automa cuando se cree el registro
    updated = models.DateTimeField(auto_now_add =True) #agrega la fecha automa cuando se actualice el registro

    class Meta():
        """" la clase meta  permite  cambiar a singular y plural cuando nos aparezca la tabla en el panel de administración."""
        verbose_name = "Servicio"
        verbose_name_plural ="Servicios"
        
    def __str__(self) -> str:
        return self.titulo
    
    