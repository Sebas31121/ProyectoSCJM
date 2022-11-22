from django.shortcuts import render

def paginaAterrizaje(request):
    template_name = "SCJM/Templates/Index.html"
    return render(request, template_name)