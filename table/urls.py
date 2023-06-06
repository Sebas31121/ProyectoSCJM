from django.urls import path
from .views import createMesaView,editMesaView, deleteMesaView, ListMesaView
urlpatterns = [
    path('table/list', ListMesaView.as_view(), name='table_list'),
    path('table/new', createMesaView, name='create_table'),
    path('table/<pk>/update', editMesaView, name='update_table'),
    path('table/<pk>/delete', deleteMesaView, name='delete_table'),
]
