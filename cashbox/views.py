from django.shortcuts import render
from table.models import Mesa
from django.contrib.auth.decorators import login_required
from order.models import Pedido
from table.models import Mesa

@login_required(login_url='/accounts/login/')
def cashbox(request):
    tables = Mesa.objects.all().order_by('nro_mesa')
    orders = []
    for table in tables:
        try:
            latest_order = Pedido.objects.filter(nro_mesa=table).latest('fecha_hora')
            orders.append(latest_order)
        except Pedido.DoesNotExist:
            orders.append(None)
    combined_data = zip(tables, orders)
    context = {'combined_data': combined_data}
    return render(request, 'cashbox/caja.html', context)
