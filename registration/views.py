from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import UserRegistrationForm
from django.contrib.auth.views import LogoutView 
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Usuario registrado con éxito!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, '¡Oops! Hubo un error en el formulario. Por favor, verifica los datos ingresados.')
        return super().form_invalid(form)

def profile(request):
    return render(request,'registration/profile.html')

class SignOutView(LogoutView):
    pass

@login_required(login_url='/account/login/')
def editProfileView(request, pk):
    user = get_object_or_404(User, id=pk)
    userform = UserRegistrationForm(request.POST or None, instance=user)
    template_name = 'registration/profile.html'

    if request.method == 'POST':
        if userform.is_valid():
            userform.save()
            messages.success(request, "Este usuario se actualizó con éxito")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "¡Oops! Hubo un error en el formulario. Por favor, verifica los datos ingresados.")

    return render(request, template_name, {'title': 'System SJD - Actualizar usuario', 'title_form': "Actualizar usuario", 'form': userform})