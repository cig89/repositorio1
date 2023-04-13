from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("Home")
    
    # return render(request, "proyectoWebApp\home")

def servicios(request):
    return HttpResponse("aqui son los servicios")
#     return render(request, "proyectoWebApp\servicios")

def tienda(request):
    return HttpResponse("esto es la tienda")
#     return render(request, "proyectoWebApp\tienda")

def blog(request):
    return HttpResponse("esto es el blog")
#     return render(request, "proyectoWebApp\blog")

def contacto(request):
    return HttpResponse("esto es el contacto")
#     return render(request, "proyectoWebApp\contacto")