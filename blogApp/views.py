from django.shortcuts import render
from .models import Post

def blog(request):
    lista_posts = Post.objects.all()  # Devuelve un queryset(una lista de objetos)
    return render(request, "blog.html", {"lista_posts": lista_posts} )  #el tercero argumento es para pasarle el la variable al template

