from django import forms
from .models import Category,SubCategory,Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

        def __init__(self,*arg,**kwargs) -> None:
            super().__init__(*arg,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({"class":"form-control"})