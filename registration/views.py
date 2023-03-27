from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import UserRegistrationForm
from django.contrib.auth.views import LogoutView 
from django.contrib import messages

# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Usuario registrado con éxito!')
        return response

def profile(request):
    return render(request,'registration/profile.html')

class SignOutView(LogoutView):
    pass