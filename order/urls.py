from django.urls import path
from .views import OrderSaveView, OrderView,preView
urlpatterns = [
    path('order/new/', OrderSaveView, name='order_save' ),
    path('order/table/', OrderView, name='products_waiter' ),
    path('order/preview/', preView, name= 'preview_order'),
    ]