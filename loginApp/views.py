
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from django.contrib import messages


"""METODOS PARA EL FORMULARIO DE REGISTRO"""       
def get(request): #Se crea el metodo get para mostrar el formulario en el html
    
    if request.method == "POST": #si el usuario ha pulsado el boton enviar del formulario
        form = UserCreationForm(request.POST) #Se reciben los datos que el usario envia en el formulario
    
        if form.is_valid():           #1-si los datos que envía el usuario es válido. Is_valid se utiliza para valiar los campos del formulario
            form.save()               #2-se almacena la información introducida por el usuario  en la tabla auth_user
            return redirect("Login")  #3-Se redirecciona el usuario despues de enviar el formulario
        
        else:  #si hay fallo(la contraseña no cumple las validaciones de django), le digo que los muestre para evitar el error en la pagina. utilizo el metodo error_messages del objeto form, que es una lista.
            for i  in form.error_messages: #por cada mensaje de error que haya
                messages.error(request, form.error_messages[i])
            return render (request, "loginApp/registro.html", {"form":form})

        
    else:   #si el usuario NO ha pulsado el boton, muestramo el formulario     
        form = UserCreationForm()  #se crea el formulario usando la clase que proporciona Django
        return render (request, "loginApp/registro.html", {"form":form})



"""METODOS PARA EL FORMULARIO DE LOGIN"""
def iniciar_sesion(request):
    
    if request.method == "POST": 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): #si el usuario es valido
            nombre_usuario = form.cleaned_data.get("username") #rescatamos la info del input nombre. Se llama username
            contraseña = form.cleaned_data.get("password") #rescatamos la info del input de la contraseña
            #Ahora se contrasta esta info con la BBDD. Esto no se hace  manualmente, sino con el método 'authenticate'
            usuario = authenticate(username=nombre_usuario, password=contraseña)  #con esto se autentica
            if usuario is not None: #si el usuario existe
                login(request, usuario) #lo logea y entra en la sesion
                return redirect("Home")
            else: #si el usuario NO existe
                messages.error(request, "El usuario no existe")
                return redirect("Login")

            
        else: #si el usuario no es válido
            messages.error(request, "La información es incorrecta")
            return redirect("Login")

        
    else: #si el usuario NO ha pulsado el boton, muestramo el formulario       
        #esta vista es la que muestra el formulario de registro
        form = AuthenticationForm()   #se crea un objeto de la clase AuthenticationForm, que me permite hacer login
        return render (request, "loginApp/login.html", {"form":form})


    

def cerrar_sesion(request):
    """Esta función se encarga de salir de la sesión. esta función se ejecutara mediante un botón."""
    logout(request)  #esto es un metodo de django
    return redirect("Home")