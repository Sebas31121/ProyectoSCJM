from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import UserRegistrationForm

# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
    success_menssage = 'Usuario registrado correctamente'

def profile(request):
    return render(request,'registration/profile.html')