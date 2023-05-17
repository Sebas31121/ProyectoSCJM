from django.urls import path
from .views import createMesaView,editMesaView, deleteMesaView,ListMesaView
urlpatterns = [
    path('table/list/mesa', ListMesaView.as_view(), name='mesa_list' ),
    path('table/new/mesa', createMesaView, name='table_mesa'),
    path('table/<pk>/update/mesa', editMesaView, name='table_update_mesa'),
    path('table/<pk>/delete/mesa', deleteMesaView, name='eliminar_mesa'),
]
