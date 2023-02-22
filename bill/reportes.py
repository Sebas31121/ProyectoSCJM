from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import timedelta

from .models import FacturaDetalle, FacturaBase



def imprimir_factura_recibo(request, numero_factura):
    template_name = 'factura/factura_recibo.html'

    encabezado = FacturaBase.objects.get(id=numero_factura)
    detalle = FacturaDetalle.objects.filter(factura=numero_factura)

    context = {
        'request': request,
        'enc': encabezado,
        'detalle': detalle,
    }

    return render(request, template_name, context)

def imprimir_factura_list(request,fecha_1,fecha_2):
    template_name = 'factura/factura_imprimir_todo.html'

    fecha_1 =parse_date(fecha_1)
    fecha_2=parse_date(fecha_2)
    fecha_2=fecha_2+timedelta(days=1)

    enc = FacturaBase.objects.filter(fecha__gte =fecha_1,fecha__lt=fecha_2)
    fecha_2 = fecha_2 - timedelta(days=1)

    context ={
        'request':request,
        'f1':fecha_1,
        'f2':fecha_2,
        'enc':enc,
    }

    return render(request, template_name, context)