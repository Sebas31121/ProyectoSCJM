from django.shortcuts import render
from table.models import Mesa
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def cashbox(request):
    context = []
    tables = Mesa.objects.all()
    #get total price per table
    return render(request,'cashbox/caja.html',{'tables':tables})