from django.urls import path
from .views import createCustomerView,editCustomerView, deleteCustomerView,listCustomerView
urlpatterns = [
    path('customer/list', listCustomerView.as_view(), name='customer_list'),
    path('customer/new', createCustomerView, name='create_customer'),
    path('customer/<pk>/update', editCustomerView, name='update_customer'),
    path('customer/<pk>/delete', deleteCustomerView, name='delete_table'),
]
