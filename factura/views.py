from django.shortcuts import render,redirect
from django import datetime
from django.contrib import messages
from inventory.models import Product
from django.views.generic import ListView, CreateView, UpdateView
from .models import FacturaBase, FacturaDetalle
from django.contrib.auth.decorators import login_required, permission_required

class FacturaView(ListView):
    model = FacturaBase
    template_name = 'factura/factura_list.html'
    context_object_name = 'obj'
    permission_required = 'factura.view_factura'

@login_required(login_url='/login/')
def facturas(request, id=None):
    template_name = 'factura/facturas.html'
    detalle = {}
    
    if request.method == "GET":
        enc = FacturaBase.objects.filter(pk=id).first()
        if not enc:
            encabezado = {
                'id': 0,
                'fecha': datetime.datetime.today(),
                'sub_total': 0.00,
                'descuento': 0.00,
                'total': 0.00,
            }
            detalle = None
        else:
            encabezado = {
                'id': enc.id,
                'fecha': datetime.datetime.today(),
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total,
            }
            detalle = FacturaDetalle.objects.filter(factura=enc)

        context = {"enc": encabezado, "det": detalle}

    if request.method == 'POST':
        fecha = request.POST.get("fecha")
        # si no hay id significa que la factura es nueva
        if not id:
            enc = FacturaBase(
                fecha=fecha,
                user=request.user
            )
            if enc:
                enc.save()
                id = enc.id
        else:
            enc = FacturaBase.objects.filter(pk=id).first()
            if enc:
                enc.user_modification = request.user.id
                enc.save()
        if not id:
            messages.error(request, 'No se detecto ningun numero de factura')
            return redirect('factura_list')

        codigo = request.POST.get('codigo')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        s_total = request.POST.get('sub_total_detalle')
        descuento = request.POST.get('descuento_detalle')
        total = request.POST.get('total_detalle')

        pro = Product.objects.get(codigo=codigo)
        det = FacturaBase(
            factura=enc,
            producto=pro,
            cantidad=cantidad,
            precio=precio,
            sub_total=s_total,
            descuento=descuento,
            total=total,
        )
        if det:
            det.save()
        return redirect('factura_edit', id=id)

    return render(request, template_name, context)
