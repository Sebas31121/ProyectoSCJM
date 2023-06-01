from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import CategoryForm, ProductForm, UnityForm,DeleteForm
from .models import Category, Product,Unity
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def createCategoryView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=CategoryForm()
    if request.method=='POST':
        form_inventory=CategoryForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
            messages.success(request=request, message="Esta categoría se creó con éxito")
            return HttpResponseRedirect('/inventory/list/product')

    return render(request,template_name,{'title':'SCJM-Crear Categoria','title_form':"Crear Categoria",'form':form_inventory})

@login_required(login_url='/accounts/login/')
def editCategoryView (request,pk):
    category = get_object_or_404(Category,id=pk)
    categoryform = CategoryForm(request.POST or None,instance=category)
    template_name = 'inventory/inventory_form.html'
    if categoryform.is_valid():
        categoryform.save()
        messages.success(request=request, message="Esta categoría se actualizó con éxito")
        return HttpResponseRedirect('/inventory/list/product')

    return render(request,template_name,{'title':'SCJM-Actualizar Categoria','title_form':"Actualizar Categoria",'form':categoryform,"obj":category})
    
@login_required(login_url='/account/login/')
def createProductView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=ProductForm()
    if request.method=='POST':
        form_inventory=ProductForm(request.POST,request.FILES)
        if form_inventory.is_valid():
            form_inventory.save()
            messages.success(request=request, message="Este producto se creó con éxito")
        return HttpResponseRedirect('/inventory/list/product')
    return render(request,template_name,{'title':'SCJM-Crear Producto','title_form':"Crear Producto",'form':form_inventory})

class ListProductView(ListView):
    template_name = "inventory/inventory_list.html"
    model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(is_active=True)

@login_required(login_url='/account/login/')
def editProductView (request, pk):
    product = get_object_or_404(Product, id=pk)
    productform = CategoryForm(request.POST or None,instance=product)
    template_name = 'inventory/inventory_form.html'
    if productform.is_valid():
        productform.save()
        messages.success(request=request, message="Este producto se actualizó con éxito")
        return HttpResponseRedirect('/inventory/list/product')
    return render(request,template_name,{'title':'SCJM-Actualizar Producto','title_form':"Actualizar Producto",'form':productform})

@login_required(login_url='/account/login/')
def createUnityView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=UnityForm()
    if request.method=='POST':
        form_inventory=UnityForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
            messages.success(request=request, message="Este unidad de medida se creó con éxito")
            return HttpResponseRedirect('/inventory/list/product')
    return render(request,template_name,{'title':'SCJM-Crear Unidad de medida','title_form':"Crear unidad de medida",'form':form_inventory})

@login_required(login_url='/account/login/')
def deleteProductView(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.is_active=False
    product.save()
    messages.success(request=request, message="Este producto se eliminó con éxito")
    return HttpResponseRedirect('/inventory/list/product')