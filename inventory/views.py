from django.shortcuts import render
from .forms import CategoryForm,SubCategoryForm

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