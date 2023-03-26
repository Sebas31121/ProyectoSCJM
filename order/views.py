from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from order.forms import PedidoForm
from inventory.models import Product
from .models import Pedido
from order.order import Order

@login_required(login_url='/accounts/login/')
def saveOrderView(request):
    template_name='order/waiter.html'
    form_pedido={}
    active_products=Product.objects.filter(is_active=True)
    if request.method=='GET':
        form_pedido=PedidoForm()
    if request.method=='POST':
        form_pedido=PedidoForm(request.POST)
        if form_pedido.is_valid():
            form_pedido.save()
    return render(request,template_name,{'title':'SCJM-Guardar Pedido','title_form':"Guardar Pedido",'form':form_pedido,'all_products':active_products})

@login_required(login_url='/accounts/login/')
def OrderView(request):
    template_name='order/products_waiter.html'
    form_pedido={}
    active_products=Product.objects.filter(is_active=True)
    if request.method=='GET':
        form_pedido=PedidoForm()
    if request.method=='POST':
        form_pedido=PedidoForm(request.POST)
        if form_pedido.is_valid():
            form_pedido.save()
    return render(request,template_name,{'title':'SCJM-Guardar Pedido','title_form':"Guardar Pedido",'form':form_pedido,'all_products':active_products})

@login_required(login_url='/accounts/login/')
def preView(request):
    template_name='order/preview.html'
    producto= Product.objects.all()
    return render(request,template_name, {'productos':producto})

@login_required(login_url='/accounts/login/')
def agregar_producto(request,producto_id):
    order = Order(request)
    producto = Product.objects.get(id=producto_id)
    order.agregar(producto)
    return redirect("order:products_waiter")

@login_required(login_url='/accounts/login/')
def eliminar_producto (request, producto_id):
    order = Order(request)
    producto = Product.objects.get(id=producto_id)
    order.eliminar_order(producto)
    return redirect("order:products_waiter")

@login_required(login_url='/accounts/login/')
def restar (request, producto_id):
    order = Order(request)
    producto = Product.objects.get(id=producto_id)
    order.restar(producto)
    return redirect("order:products_waiter")

@login_required(login_url='/accounts/login/')
def limpiar (request, producto_id):
    order = Order(request)
    order.limpiar()
    return redirect("order:products_waiter")