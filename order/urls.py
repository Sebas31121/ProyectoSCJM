from django.urls import path,include
from .views import saveOrderView
urlpatterns = [
    path('order/new/', saveOrderView, name='order_new' ),]