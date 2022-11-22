from django.urls import path,include
from .views import inventoryView
urlpatterns = [
    path('inventory/new/', inventoryView, name='inventory' )
]