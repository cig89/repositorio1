from django import forms

class FormularioContacto(forms.Form):
    nombre    = forms.CharField(label = "Nombre", required = True, max_length = 20)
    email     = forms.CharField(label = "Email",   required = True,  max_length=100)
    contenido = forms.CharField(label = "Contenido", required =True, widget=forms.Textarea)  #textArea permite ampliar el cuadro de insercción de texto en la web
    