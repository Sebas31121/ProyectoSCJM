from django.urls import path,include
from .views import saveOrderView, OrderView
urlpatterns = [
    path('order/new/', saveOrderView, name='order_new' ),
    path('order/table/', OrderView, name='products_waiter' ),]