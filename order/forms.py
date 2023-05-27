from django import forms
from .models import Pedido,Mesa


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nro_mesa']

    def __init__(self, *args, **kwargs) -> None:
        super(MesaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['id','estado','nro_mesa']

    def __init__(self, *args, **kwargs) -> None:
        super(PedidoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field=="nro_mesa":
                self.fields[field].widget.attrs.update({'class': 'form-control','display':'none'})
            self.fields[field].widget.attrs.update({'class': 'form-control'})       