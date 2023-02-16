from django.urls import path,include
from .views import createCategoryView,createSubcategoryView,createProductView,editCategoryView,editSubcategoryView,editProductView,ListProductView
urlpatterns = [
    path('inventory/list/product', ListProductView.as_view(), name='inventory_list' ),
    path('inventory/new/category', createCategoryView, name='inventory_category' ),
    path('inventory/new/subcategory', createSubcategoryView, name='inventory_subcategory' ),
    path('inventory/new/product', createProductView, name='inventory_product'),
    path('inventory/<pk>/update/category', editCategoryView, name='inventory_update_category'),
    path('inventory/<pk>/update/subcategory', editSubcategoryView, name='inventory_update_subcategory'),
    path('inventory/<pk>/update/product', editProductView, name='inventory_update_product'),
]