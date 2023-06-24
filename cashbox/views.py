from django.shortcuts import render, redirect
from table.models import Mesa
from django.contrib.auth.decorators import login_required
from order.models import Pedido
from table.models import Mesa

def access_barra(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='Barras').exists():
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

@access_barra
@login_required(login_url='/accounts/login/')
def cashbox(request):
    tables = Mesa.objects.all().order_by('nro_mesa')
    context = {'tables': tables}
    return render(request, 'cashbox/caja.html', context)

@login_required(login_url='/accounts/login/')
def searchOrder(request, pk):
    table_number = Mesa.objects.filter(id=pk)
    Pedido.objects.filter(nro_mesa=table_number)
