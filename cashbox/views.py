from django.shortcuts import render, get_object_or_404
from table.models import Mesa
from django.contrib.auth.decorators import login_required
from order.models import Pedido
from table.models import Mesa

@login_required(login_url='/accounts/login/')
def cashbox(request):
    context = []
    tables = Mesa.objects.all().order_by('nro_mesa')
    #get total price per table
    return render(request,'cashbox/caja.html',{'tables':tables})

@login_required(login_url='/accounts/login/')
def viewOrderCashbox(request,pk):
    pedido_actual= Pedido.objects.filter(nro_mesa=pk)
    if pedido_actual.estado=="Pendiente":
        nada=1
    return render(request,'cashbox/pedido_caja.html')