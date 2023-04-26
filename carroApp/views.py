from django.shortcuts import render

from shopApp.models import *

from django.shortcuts import redirect 

class Carro:
    
    def __init__(self,request):
        
        self.request = request
        self.session = request.session  #iniciamos la sesion
        
        carro = self.session.get("carro")
        
        ''' creamos o recuperamos el carro en la sesion si el usuario inicia sesión o vuelve a la sesión ya iniciada. '''
        
        if not carro: # si no existe ningún carro al iniciar la sesión, se crea uno nuevo. Este será un dic: { id_producto1: {nombre: xxx, precio: xxx, imagen:xxx,...}, id_producto2:...}
            carro = self.session["carro"] = {} #se crea una sesión nueva
        self.carro = carro  #si existe un carro en esa sesión, se utiliza el que exista. Esto es cuando el usuario sale de la pagina tienda pero no cierra el navegador y luego vuelve.

            
        
    def agregar_producto(self, producto):
        """Esta funcion hace dos cosas: 
        1-Si el producto NO existe en el carro, añade el producto al carro 
        2-Si el producto SI existe en el carro, añade una unidad"""
        
        #1º-Si el producto NO existe en el carro, hay que agregarlo
        if str(producto.id) not in  self.carro.keys(): #si el producto NO está en el carro, hay que añadir uno nuevo. Por tanto, si no existe en las claves del diccionario...
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url
            }       
        #2º-Si el producto SI existe en el carro, hay que añadir una unidad
        else: #si existe el producto en el carro, hay que incrementar en 1 la cantidad
            for key,value in self.carro.items(): #se itera los productos del carro...
                if key ==str(producto.id):  #si alguna key coindice con el producto.id...
                    value["cantidad"] += 1  #se incrementa en uno...
                    
        self.guardar_carro()  # esto actualizará la sesión 
        
    def restar_producto(self,producto):                      
        """Esta funcion resta una unidad al producto del carro si existe el producto. Si no existe dicho producto, no hace nada"""
        for key,value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"] = value["cantidad"] -1
                if value["cantidad"] <1:
                    self.eliminar_producto(producto)
        self.guardar_carro()   
                        

    def eliminar_producto(self,producto):
        """Esta función se encarga de elminar un producto del carro, es decir, un producto con todas sus undiades. 
        No confudir con restar, la cual, no elimina el producto, sino solo una unidad de dicho producto."""
        
        #1º-se comprueba que el prducto a eliminar esta en el carro
        producto.id = str(producto.id)  #pasamos el id a string
        if producto.id in self.carro:   #se comprueba si esta en el carro
            del self.carro[producto.id] #si esta, se elimina
            self.guardar_carro()        #se llama a la función guardar_carro para actualizar el carro
            
    def eliminar_todos_productos(self):
        """esta función elimina TODOS los productos, es decir, vacía el carro"""
        carro = self.session["carro"] = {}        
        self.session.modified =True
        
                
    def guardar_carro(self):
        """esta funcion se encarga de guardar o actualizar el carro cuando se añade/reste/elimine algún producto"""
        self.session["carro"] = self.carro  # Actualiza el carro
        self.session.modified = True
        

#SE CREAN LAS VISTAS

def agregar_producto_vista(request,producto_id):
    
    #accedemos al producto que viene por parámetro    
    producto = Producto.objects.get(pk=producto_id)
    
    #ahora se crea el carro y se llama a la funcion agregar_producto
    carro = Carro(request)
    carro.agregar_producto(producto =producto)
    return redirect("Shop")   #Redireccionamos a la tienda. Dentro del redirect metemos la url, es decir, el nombre que le pusimos a la url de la tienda

def restar_producto_vista(request,producto_id):
    
    #accedemos al producto que viene por parámetro    
    producto = Producto.objects.get(pk=producto_id)
    
    #ahora se crea el carro y se llama a la funcion restar_producto
    carro = Carro(request)
    carro.restar_producto(producto =producto)
    return redirect("Shop")   #Redireccionamos a la tienda. Dentro del redirect metemos la url, es decir, el nombre que le pusimos a la url de la tienda

def eliminar_producto_vista(request,producto_id):
    
    #accedemos al producto que viene por parámetro    
    producto = Producto.objects.get(pk=producto_id)
    
    #ahora se crea el carro y se llama a la funcion eliminar_producto
    carro = Carro(request)
    carro.eliminar_producto(producto =producto)
    return redirect("Shop")   #Redireccionamos a la tienda. Dentro del redirect metemos la url, es decir, el nombre que le pusimos a la url de la tienda
        
            
def eliminar_todos_productos_vista(request):

    #ahora se crea el carro y se llama a la funcion eliminar_todos_productos. No se le pasa nada por parámetro porque se elimina todo del carro
    carro = Carro(request)
    carro.eliminar_todos_productos()
    return redirect("Shop")   #Redireccionamos a la tienda. Dentro del redirect metemos la url, es decir, el nombre que le pusimos a la url de la tienda
        
