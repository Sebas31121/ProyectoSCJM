from django.http import HttpResponse
from django.template.loader import get_template
from django.urls import reverse
from django.views import View
from reportlab.pdfgen import canvas
from .models import Factura
from django.shortcuts import redirect

class FacturaPDFView(View):
    def get(self, request, *args, **kwargs):
        # Obtén los datos de la factura y los productos
        factura = Factura.objects.get(pk=kwargs['factura_id'])
        productos = factura.productos.all()

        # Crea el objeto PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="factura.pdf"'
        p = canvas.Canvas(response)

        # Agrega los datos de la factura al PDF
        p.drawString(100, 100, f'Número de factura: {factura.numero}')
        p.drawString(100, 120, f'Fecha: {factura.fecha}')
        # Agrega más detalles de la factura...

        # Agrega los productos al PDF
        y = 200
        for producto in productos:
            p.drawString(100, y, f'Producto: {producto.nombre}')
            p.drawString(100, y + 20, f'Precio: {producto.precio}')
            # Agrega más detalles del producto...
            y += 40

        p.showPage()
        p.save()
        return response

def generar_factura(request, factura_id):
    # Lógica para generar la factura...
    factura = Factura.objects.get(pk=factura_id)

    # Obtén el enlace al PDF de la factura
    pdf_url = reverse('factura_pdf', kwargs={'factura_id': factura.id})

    # Haz algo con el enlace al PDF...
    return redirect(pdf_url)