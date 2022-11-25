from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import CategoryForm,SubCategoryForm,ProductForm
from .models import Category,SubCategory,Product
def createCategoryView (request):
    template_name='inventory/inventory_form.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=CategoryForm()
    if request.method=='POST':
        name=request.POST.get("name")
        form_inventory=CategoryForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
    return render(request,template_name,{'title':'SCJM-Crear Categoria','form':form_inventory})

def editCategoryView (request,pk):
    category = get_object_or_404(Category,id=pk)
    categoryform = CategoryForm(request.POST or None,instance=category)
    template_name = 'inventory/inventory_form.html'
    if categoryform.is_valid():
        categoryform.save()
        return HttpResponseRedirect('/inventory/new/category')

    return render(request,template_name,{'title':'SCJM-Actualizar Categoria','form':categoryform})
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
    return render(request,template_name,{'title':'SCJM-Crear Subcategoria','form':form_inventory})

def editSubcategoryView (request,pk):
    subcategory = get_object_or_404(SubCategory,id=pk)
    subcategoryform = CategoryForm(request.POST or None,instance=subcategory)
    template_name = 'inventory/inventory_form.html'
    if subcategoryform.is_valid():
        subcategoryform.save()
        return HttpResponseRedirect('/inventory/new/subcategory')

    return render(request,template_name,{'title':'SCJM-Actualizar Subcategoria','form':subcategoryform})

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
    return render(request,template_name,{'title':'SCJM-Crear Producto','form':form_inventory})

def editProductView (request,pk):
    product = get_object_or_404(Product,id=pk)
    productform = CategoryForm(request.POST or None,instance=product)
    template_name = 'inventory/inventory_form.html'
    if productform.is_valid():
        productform.save()
        return HttpResponseRedirect('/inventory/new/product')

    return render(request,template_name,{'title':'SCJM-Actualizar Producto','form':productform})
