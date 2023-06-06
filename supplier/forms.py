from django import forms
from .models import Proveedor

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nit', 'nombre', 'contacto', 'ubicacion']

    def __init__(self, *args, **kwargs) -> None:
        super(SupplierForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
