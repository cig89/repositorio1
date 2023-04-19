from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    """esta clase permitirá clasificar los posts  en categorías"""
    nombre =  models.CharField(    max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    """en este modelo se guardarán los post creados. Cada post, estará asociado a un usuario(autor) y a una categoría"""
    titulo =     models.CharField(max_length=50)
    contenido =  models.TextField()
    imagen =     models.ImageField(upload_to="blogApp", null =True, blank = True)
    autor =      models.ForeignKey(User, on_delete=models.CASCADE) #establecemos la relacion 1:N entre la tabla User predefinida en Django y la tabla Post
    categorias = models.ManyToManyField(Categoria)  #establecemos la relacion N:M entre la tabla Post y Categorias( un post puede estar en varias categorias y viceversa). Si eliminamos el autor=> se eliminarán sus posts.
    created =    models.DateTimeField(auto_now_add=True)
    updated =    models.DateTimeField(auto_now_add=True)  
    
    class Meta():
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.titulo
    