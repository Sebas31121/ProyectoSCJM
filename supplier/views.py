from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .models import Proveedor
from .forms import SupplierForm
from django.views.generic import ListView

@login_required(login_url='/account/login/')
def createSupplierView (request):
    template_name='supplier/supplier_view.html'
    form_supplier={}
    if request.method=='GET':
        form_supplier=SupplierForm()
    if request.method=='POST':
        form_supplier=SupplierForm(request.POST,request.FILES)
        if form_supplier.is_valid():
            form_supplier.save()
            messages.success(request=request, message="El proveedor ha sido creado con éxito")
        return HttpResponseRedirect('/supplier/list')
    return render(request,template_name,{'title':'SCJM-Crear proveedor','title_form':"Crear proveedor",'form':form_supplier})

@login_required(login_url='/account/login/')
def editSupplierView (request, pk):
    proveedor = get_object_or_404(Proveedor, id=pk)
    proveedorform = SupplierForm(request.POST or None,instance=proveedor)
    template_name = 'supplier/supplier_view.html'
    if proveedorform.is_valid():
        proveedorform.save()
        messages.success(request=request, message="El proveedor se actualizó con exito")
        return HttpResponseRedirect('/supplier/list')
    return render(request,template_name,{'title':'SCJM-Actualizar proveedor','title_form':"Actualizar proveedor",'form':SupplierForm})

@login_required(login_url='/account/login/')
def deleteSupplierView(request, pk):
    proveedor = get_object_or_404(Proveedor, id=pk)
    proveedor.is_active=False
    proveedor.save()
    messages.success(request=request, message="El proveedor se eliminó con éxito")
    return HttpResponseRedirect('/supplier/list')

class listSupplierView(ListView):
    template_name = 'supplier/supplier_list.html'
    model = Proveedor
    context_object_name = "proveedors"
    queryset = Proveedor.objects.filter(is_active=True)