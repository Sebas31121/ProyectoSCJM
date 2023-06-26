from django.urls import path
from .views import cashbox,paidOrder,get_orders

urlpatterns = [
    path( 'caja/', cashbox, name="cashbox"),
    path('order/get/',get_orders),
    path('order/paid/', paidOrder,name="paid_order"),
]