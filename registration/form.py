from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

    def __init__(self, *arg, **kwargs) -> None:
        super(UserRegistrationForm, self).__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({"class": "form-control mt-1"})
            if field=="email":
                self.fields[field].widget.attrs.update({'class': 'form-control','readonly': True})