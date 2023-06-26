import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from table.models import Mesa
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from order.models import Pedido,ProductOrder,Product
from table.models import Mesa

def access_barra(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='Barras').exists():
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def get_orders(request):
    tables = Mesa.objects.all().order_by('nro_mesa')
    orders = []
    for table in tables:
        try:
            latest_order = Pedido.objects.filter(nro_mesa=table, estado=1).latest('fecha_hora')
            orders.append(latest_order)
        except Pedido.DoesNotExist:
            orders.append(None)
    combined_data = zip(tables, orders)
    
    
    combined_list = [(str(table), serializers.serialize('json', [order]) if order else None) for table, order in combined_data]
    
    # return como JSON response
    return JsonResponse(combined_list, safe=False)


@access_barra
@login_required(login_url='/accounts/login/')
def cashbox(request):
    return render(request, 'cashbox/caja.html')

@csrf_exempt
def paidOrder(request):
    data = json.loads(request.body.decode("utf-8"))
    order = Pedido.objects.get(id=data.get("pk_order"))
    order.estado = 2
    order.save()

    return JsonResponse({"success":True})