from django.urls import path
from .views import createCategoryView,createProductView,editCategoryView,editProductView,ListProductView,createUnityView,deleteProductView, product_detail, DownloadPDFView
urlpatterns = [
    path('inventory/list/product', ListProductView.as_view(), name='inventory_list' ),
    path('inventory/new/category', createCategoryView, name='inventory_category' ),
    path('inventory/new/product', createProductView, name='inventory_product'),
    path('inventory/new/unity', createUnityView, name='inventory_unity'),
    path('inventory/<pk>/update/category', editCategoryView, name='inventory_update_category'),
    path('inventory/<pk>/update/product', editProductView, name='inventory_update_product'),
    path('inventory/<pk>/delete/product', deleteProductView, name='eliminar_producto'),
    path('detalle/<pk>/product', product_detail, name='detalle_producto'),
    path('products/pdf/', DownloadPDFView.as_view(), name='download_pdf'),
]