from django.shortcuts import render
from table.models import Mesa
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Table

@login_required(login_url='/accounts/login/')
def cashbox(request):
<<<<<<< HEAD
    context = []
    tables = Mesa.objects.all()
    #get total price per table
    return render(request,'cashbox/caja.html',{'tables':tables})
=======
    return render(request,'cashbox/caja.html')

def listar_mesas(request):
    all_tables = Table.objects.all()
    return render(request, 'cashbox/caja.html', {'all_tables': all_tables})

class tablesViews(ListView):
    template_name = "cashbox/caja.html"
    model = Table
    context_object_name = "tables"
    """queryset = Table.objects.filter(is_active=True)"""
>>>>>>> refs/remotes/origin/main
