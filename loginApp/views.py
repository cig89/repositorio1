
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib import messages


        
def get(request): #Se crea el metodo get para mostrar el formulario en el html
    form = UserCreationForm()  #se crea el formulario usando la clase que proporciona Django
    return render (request, "loginApp/registro.html", {"form":form})

def post(request): #se crea el motodo post para gestionar la recepción dle formulario y la redirección
    form = UserCreationForm(request.POST) #Se reciben los datos que el usario envia en el formulario
    
    if form.is_valid(): #si los datos que envía el usuario es válido. Is_valid se utiliza para valiar los campos del formulario
        #3-Se redirecciona el usuario despues de enviar el formulario
        return redirect("Home") 
    
    else:  #si hay algún fallo, le digo que los muestre para evitar el error en la pagina. utilizo el metodo error_messages del objeto form, que es una lista.
        for i  in form.error_messages: #por cada mensaje de error que haya
            messages.error(request, form.error_messages[i])
            
        return render (request, "loginApp/registro.html", {"form":form})