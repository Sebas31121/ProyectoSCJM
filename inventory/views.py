from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import CategoryForm, ProductForm, UnityForm
from .models import Category, Product
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
def createProductView(request):
    template_name = 'inventory/inventory_form.html'
    form_inventory = {}
    if request.method == 'GET':
        form_inventory = ProductForm()

    if request.method == 'POST':
        form_inventory = ProductForm(request.POST, request.FILES)
        if form_inventory.is_valid():
            form_inventory.save()
            messages.success(request=request, message="Este producto se creó con éxito")
            return HttpResponseRedirect('/inventory/list/product')

    return render(request, template_name, {'title': 'SCJM-Crear Producto', 'title_form': "Crear Producto", 'form': form_inventory})

class ListProductView(ListView):
    template_name = "inventory/inventory_list.html"
    model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(is_active=True)

@login_required(login_url='/account/login/')
def editProductView(request, pk):
    product = get_object_or_404(Product, id=pk)
    template_name = 'inventory/inventory_form.html'
    if request.method == 'POST':
        productform = ProductForm(request.POST, instance=product, is_edit=True)
        if productform.is_valid():
            productform.save()
            messages.success(request=request, message="Este producto se actualizó con éxito")
            return HttpResponseRedirect('/inventory/list/product')
    else:
        productform = ProductForm(instance=product, is_edit=True)
    return render(request, template_name, {'title': 'SCJM-Actualizar Producto', 'title_form': "Actualizar Producto", 'form': productform})


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

@login_required(login_url='/account/login/')
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        action = request.POST['action']

        if action == 'add':
            product.stock += quantity
            messages.success(request, f'Se agregaron {quantity} unidades al stock de {product.name}.')
        elif action == 'subtract':
            if quantity > product.stock:
                messages.error(request, 'La cantidad ingresada es mayor al stock actual.')
            else:
                product.stock -= quantity
                messages.success(request, f'Se restaron {quantity} unidades al stock de {product.name}.')

        product.save()
        return redirect('inventory_list')

    template_name = 'inventory/product_detail.html'
    context = {
        'product': product,
    }
    return render(request, template_name, context)
