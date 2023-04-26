from django.http import HttpResponse
from .views import Carro

def importe_total_carro(request):
    total =25  
    carro = Carro(request)
    
    if request.user.is_authenticated:
        for key,value in request.session["carro"].items():
            total = total + (float(value["precio"]))*value["cantidad"]
            

    return {"importe_total": total }

