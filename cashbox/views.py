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

            products_order = ProductOrder.objects.filter(order=latest_order)
            product_list = [
                {
                    'name': product_order.product.name,
                    'price': float(product_order.product.price),
                } for product_order in products_order
            ]
            
            orders.append({
                'id': latest_order.id,
                #'fecha_hora': latest_order.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),
                'estado': latest_order.get_estado_display(),
                'nro_mesa': latest_order.nro_mesa.nro_mesa,
                #'autor_username': latest_order.autor_usuario.username,
                'total_pedido': float(latest_order.total_pedido),
                'products': product_list
            })
        except Pedido.DoesNotExist:
            print("PEDIDO NO EXISTE")
    
    # return como JSON response
    return JsonResponse(orders, safe=False)


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