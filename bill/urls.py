from django.urls import path
from .views import FacturaPDFView

urlpatterns = [
    # Otras URLs...
    path('facturas/<int:factura_id>/pdf/', FacturaPDFView.as_view(), name='factura_pdf'),
]
