from django.urls import path
from .views import cashbox

urlpatterns = [
    path( 'caja/', cashbox, name="cashbox"),

]