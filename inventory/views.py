from django.shortcuts import render
from .forms import CategoryForm

def inventoryView (request):
    template_name='inventory/index.html'
    form_inventory={}
    if request.method=='GET':
        form_inventory=CategoryForm()
    if request.method=='POST':
        name=request.POST.get("name")
        form_inventory=CategoryForm(request.POST)
        if form_inventory.is_valid():
            form_inventory.save()
    return render(request,template_name,{'title':'SCJM-inicio','form':form_inventory})