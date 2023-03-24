from django import forms
from .models import Category, SubCategory, Product, Unity


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs) -> None:
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']

    def __init__(self, *arg, **kwargs) -> None:
        super(SubCategoryForm, self).__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control mt-1'})

class UnityForm(forms.ModelForm):
    class Meta:
        model = Unity
        fields = ['name']

    def __init__(self, *arg, **kwargs) -> None:
        super(UnityForm, self).__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({"class": "form-control mt-1"})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock','img_route', 'unity','category','subcategory']

    def __init__(self, *arg, **kwargs) -> None:
        super(ProductForm, self).__init__(*arg, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({"class": "form-control mt-1"})