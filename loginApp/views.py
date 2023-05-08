
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib import messages


class VistaRegistro(View):
    def get(self, request): #Se crea el metodo get para mostrar el formulario en el html
        form = UserCreationForm()  #se crea el formulario usando la clase que proporciona Django
        return render (request, "loginApp/registro.html", {"form":form})

    def post(self, request): #se crea el motodo post para gestionar la recepción dle formulario y la redirección
        form = UserCreationForm(request.POST) #Se reciben los datos que el usario envia en el formulario
        
        if form.is_valid(): #si los datos que envía el usuario es válido. Is_valid se utiliza para valiar los campos del formulario
            # 1-se almacena la información introducida por el usuario  en la tabla auth_user
            usuario = form.save() 
            # 2-Cuando se guarden los datos, el usuario tiene que estar logeado. Esto lo gestiona el objeto login. Se le introduce el request y los datos.
            login(request,usuario)
            #3-Se redirecciona el usuario despues de enviar el formulario
            return redirect("Home") 
        
        else:  #si hay algún fallo, le digo que los muestre para evitar el error en la pagina. utilizo el metodo error_messages del objeto form, que es una lista.
            for i  in form.error_messages: #por cada mensaje de error que haya
                messages.error(request, form.error_messages[i])
                
            return render (request, "loginApp/registro.html", {"form":form})
        
