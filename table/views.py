from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib import messages
from .models import Mesa
from .forms import MesaForm
from django.views.generic import ListView

def is_staff(user):
    if user.is_staff:
        return True
    else:
        return False

def check_staff_access(view_func):
    def wrapper(request, *args, **kwargs):
        if not is_staff(request.user):
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

@check_staff_access
@login_required(login_url='/account/login/')
def createMesaView (request):
    template_name='table/table_view.html'
    form_mesa={}
    if request.method=='GET':
        form_mesa=MesaForm()
    if request.method=='POST':
        form_mesa=MesaForm(request.POST,request.FILES)
        if form_mesa.is_valid():
            form_mesa.save()
            messages.success(request=request, message="Mesa creada con éxito")
        return HttpResponseRedirect('/table/list')
    return render(request,template_name,{'title':'SCJM-Crear Mesa','title_form':"Crear Mesa",'form':form_mesa})

@check_staff_access
@login_required(login_url='/account/login/')
def editMesaView (request, pk):
    mesa = get_object_or_404(Mesa, id=pk)
    mesaform = MesaForm(request.POST or None,instance=mesa)
    template_name = 'table/table_view.html'
    if mesaform.is_valid():
        mesaform.save()
        messages.success(request=request, message="La mesa se actualizó con exito")
        return HttpResponseRedirect('/table/list')
    return render(request,template_name,{'title':'SCJM-Actualizar Mesa','title_form':"Actualizar Mesa",'form':mesaform})

@check_staff_access
@login_required(login_url='/account/login/')
def deleteMesaView(request, pk):
    mesa = get_object_or_404(Mesa, id=pk)
    mesa.is_active=False
    mesa.save()
    messages.success(request=request, message="La mesa se eliminó con éxito")
    return HttpResponseRedirect('/table/list')

class ListMesaView(ListView):
    template_name = "table/table_list.html"
    model = Mesa
    context_object_name = "mesas"
    queryset = Mesa.objects.filter(is_active=True)