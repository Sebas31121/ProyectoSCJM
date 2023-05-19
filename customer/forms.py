from django import forms
from .models import Cliente


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nickname', 'celular', 'deuda', 'abono', 'estado']

    def __init__(self, *args, **kwargs) -> None:
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
