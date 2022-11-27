from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import CategoryForm,SubCategoryForm,ProductForm
from .models import Category,SubCategory,Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def createCategoryView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=CategoryForm()
    if request.method=='POST':
        form_inventory=CategoryForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
    return render(request,template_name,{'title':'SCJM-Crear Categoria','title_form':"Crear Categoria",'form':form_inventory})

@login_required(login_url='/account/login/')
def editCategoryView (request,pk):
    category = get_object_or_404(Category,id=pk)
    categoryform = CategoryForm(request.POST or None,instance=category)
    template_name = 'inventory/inventory_form.html'
    if categoryform.is_valid():
        categoryform.save()
        return HttpResponseRedirect('/inventory/new/category')

    return render(request,template_name,{'title':'SCJM-Actualizar Categoria','title_form':"Actualizar Categoria",'form':categoryform,"obj":category})

@login_required(login_url='/account/login/')
def createSubcategoryView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=SubCategoryForm()
    if request.method=='POST':
        name=request.POST.get("name")
        form_inventory=SubCategoryForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
    return render(request,template_name,{'title':'SCJM-Crear Subcategoria','title_form':"Crear Subcategoria",'form':form_inventory})
@login_required(login_url='/account/login/')
def editSubcategoryView (request,pk):
    subcategory = get_object_or_404(SubCategory,id=pk)
    subcategoryform = CategoryForm(request.POST or None,instance=subcategory)
    template_name = 'inventory/inventory_form.html'
    if subcategoryform.is_valid():
        subcategoryform.save()
        return HttpResponseRedirect('/inventory/new/subcategory')

    return render(request,template_name,{'title':'SCJM-Actualizar Subcategoria','title_form':"Actualizar Subcategoria",'form':subcategoryform})
@login_required(login_url='/account/login/')
def createProductView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=ProductForm()
    if request.method=='POST':
        name=request.POST.get("name")
        form_inventory=ProductForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
    return render(request,template_name,{'title':'SCJM-Crear Producto','title_form':"Crear Producto",'form':form_inventory})
@login_required(login_url='/account/login/')
def editProductView (request,pk):
    product = get_object_or_404(Product,id=pk)
    productform = CategoryForm(request.POST or None,instance=product)
    template_name = 'inventory/inventory_form.html'
    if productform.is_valid():
        productform.save()
        return HttpResponseRedirect('/inventory/new/product')

    return render(request,template_name,{'title':'SCJM-Actualizar Producto','title_form':"Actualizar Producto",'form':productform})
