from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormularioContacto

from django.core.mail import EmailMessage

from ProyectoWeb import settings

def contacto(request):
    formulario_contacto = FormularioContacto()
    
    if request.method =="POST": # igualamos a POST porque este metodo se encaga de recoger los datos que envia el usuario con el post
        formulario_contacto = FormularioContacto(data = request.POST)  #Obtenemos la info intorducida en el formulario
        if formulario_contacto.is_valid():                             #Antes de acceder a los datos, hay que validarla
            nombre = request.POST.get("nombre")                        
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            #enviamos un correo 
            email =EmailMessage(
                subject="email enviado desde video-Shop con Django",
                body=f"el usuario con nombre: '{nombre}' y correo: '{email}' envia lo siguiente\n\n: {contenido}",
                from_email = settings.EMAIL_HOST_USER , 
                to=[""] 
                ) 
        
            try :
                email.send()
                #si todo ha salido correctamente, le mostramos el template de información enviada
                return   render(request, "contactoApp/contacto_informacion_enviada.html",)      
            except:
                #si algo no ha salido bien:
                return  render(request, "contactoApp/contacto_informacion_NoEnviada.html",) 
            
    return render(request, "contactoApp/contacto.html", { "miFormulario" :formulario_contacto})
