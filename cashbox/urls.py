from django.urls import path
from .views import cashbox,viewOrderCashbox

urlpatterns = [
    path( 'caja/', cashbox, name="cashbox"),
    path('order/<pk>/view', viewOrderCashbox, name="view_order" ),
]