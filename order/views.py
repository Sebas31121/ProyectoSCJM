from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from order.forms import PedidoForm
from inventory.models import Product

@login_required(login_url='/accounts/login/')
def saveOrderView(request):
    template_name='order/waiter.html'
    form_pedido={}
    all_products=Product.objects.all()
    if request.method=='GET':
        form_pedido=PedidoForm()
    if request.method=='POST':
        form_pedido=PedidoForm(request.POST)
        if form_pedido.is_valid():
            form_pedido.save()
    return render(request,template_name,{'title':'SCJM-Guardar Pedido','title_form':"Guardar Peiddo",'form':form_pedido,'all_products':all_products})
