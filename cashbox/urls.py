from django.urls import path
from .views import cashbox,paidOrder

urlpatterns = [
    path( 'caja/', cashbox, name="cashbox"),
    path('order/paid/', paidOrder,name="paid_order"),
]