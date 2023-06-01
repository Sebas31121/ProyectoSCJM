from django.urls import path
from .views import cashbox, tablesViews


urlpatterns = [
    path( 'caja/', cashbox, name="cashbox"),
    path('table/list', tablesViews.as_view(), name='table_list'),

]