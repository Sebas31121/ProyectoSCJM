from django.urls import path
from .views import createSupplierView,editSupplierView, deleteSupplierView, listSupplierView
urlpatterns = [
    path('supplier/list', listSupplierView.as_view(), name='supplier_list'),
    path('supplier/new', createSupplierView, name='create_supplier'),
    path('supplier/<pk>/update', editSupplierView, name='update_supplier'),
    path('supplier/<pk>/delete', deleteSupplierView, name='delete_supplier'),
]