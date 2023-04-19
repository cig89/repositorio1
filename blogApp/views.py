from django.shortcuts import render
from .models import Post,Categoria

def blog(request):
    lista_posts = Post.objects.all()  # Devuelve un queryset(una lista de objetos)
    return render(request, "blog.html", {"lista_posts": lista_posts} )  #el tercero argumento es para pasarle el la variable al template


def FiltroCategoria(request, categoria_id):
    ob_categoria = Categoria.objects.get(id = categoria_id)      #Se obtiene un solo objeto, que es la categoria
    lista_posts_filtrados = Post.objects.filter(categorias =ob_categoria) #Se obtiene una lista de objetos(posts) de esa categoria.
    return render(request, "filtrarPorCategoria.html", {"ob_categoria ": ob_categoria, "lista_posts_filtrados": lista_posts_filtrados  })

    