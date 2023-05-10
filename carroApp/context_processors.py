from django.http import HttpResponse
from .views import Carro

def importe_total_carro(request):
    total =0  
    carro = Carro(request)
    for key,value in request.session["carro"].items():
        total = total + float(value["precio"])
            

    return {"importe_total": total }

