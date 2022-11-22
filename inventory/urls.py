from django.urls import path,include
from .views import createCategoryView,createSubcategoryView
urlpatterns = [
    path('inventory/new/category', createCategoryView, name='inventory_category' ),
    path('inventory/new/subcategory', createSubcategoryView, name='inventory_subcategory' )
]