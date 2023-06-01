from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Table

@login_required(login_url='/accounts/login/')
def cashbox(request):
    return render(request,'cashbox/caja.html')

def listar_mesas(request):
    all_tables = Table.objects.all()
    return render(request, 'cashbox/caja.html', {'all_tables': all_tables})

class tablesViews(ListView):
    template_name = "cashbox/caja.html"
    model = Table
    context_object_name = "tables"
    """queryset = Table.objects.filter(is_active=True)"""