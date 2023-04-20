from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormularioContacto

def contacto(request):
    formulario_contacto = FormularioContacto()
    
    if request.method =="POST":
        formulario_contacto = FormularioContacto(data = request.POST)  #obtenemos la info intorducida en el formulario
        if formulario_contacto.is_valid():                             #antes de acceder a los datos, hay que validarla
            nombre = request.POST.get("nombre")                        
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            #si todo ha salido correctamente, le mostramos el template de información enviada
            return render(request, "contactoApp/contacto_informacion_enviada.html",)
            
    return render(request, "contactoApp/contacto.html", { "miFormulario" :formulario_contacto})
