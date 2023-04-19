from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Categoria

def blog(request):
    lista_posts = Post.objects.all()  # Devuelve un queryset(una lista de objetos)
    return render(request, "blog.html", {"lista_posts": lista_posts} )  #el tercero argumento es para pasarle el la variable al template


def FiltroCategoria(request, nombreCategoria):
    
    ob_categoria = Categoria.objects.filter(nombre = nombreCategoria).first()      #Se obtiene un solo objeto, que es la categoria. Si no encuentra nada, devuelve un None
    if ob_categoria == None:
        return HttpResponse(f"la categoria introducida: '{nombreCategoria}' no existe.")
    
    lista_posts_filtrados = Post.objects.filter(categorias =ob_categoria).all() #Se obtiene una lista de objetos(posts) de esa categoria.
    if lista_posts_filtrados ==None or lista_posts_filtrados ==[]:
        return HttpResponse( f" no existen posts para la categoria: {ob_categoria}" )
    
    return render(request, "filtrarPorCategoria.html", {"lista_posts_filtrados": lista_posts_filtrados  }) 

    