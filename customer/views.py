from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import CustomerForm
from django.views.generic import ListView

@login_required(login_url='/account/login/')
def createCustomerView (request):
    template_name='customer/customer_view.html'
    form_customer={}
    if request.method=='GET':
        form_customer=CustomerForm()
    if request.method=='POST':
        form_customer=CustomerForm(request.POST,request.FILES)
        if form_customer.is_valid():
            form_customer.save()
            messages.success(request=request, message="Cliente creado con éxito")
        return HttpResponseRedirect('/customer/list')
    return render(request,template_name,{'title':'SCJM-Crear cliente','title_form':"Crear cliente",'form':form_customer})

@login_required(login_url='/account/login/')
def editCustomerView (request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    clienteform = CustomerForm(request.POST or None,instance=cliente)
    template_name = 'customer/customer_view.html'
    if clienteform.is_valid():
        clienteform.save()
        messages.success(request=request, message="El cliente se actualizó con exito")
        return HttpResponseRedirect('/customer/list')
    return render(request,template_name,{'title':'SCJM-Actualizar cliente','title_form':"Actualizar cliente",'form':clienteform})

@login_required(login_url='/account/login/')
def deleteCustomerView(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    cliente.is_active=False
    cliente.save()
    messages.success(request=request, message="El cliente se eliminó con éxito")
    return HttpResponseRedirect('/customer/list')

class listCustomerView(ListView):
    template_name = "customer/customer_list.html"
    model = Cliente
    context_object_name = "clientes"
    queryset = Cliente.objects.filter(is_active=True)