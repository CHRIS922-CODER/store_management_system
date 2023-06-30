from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        is_edit_mode = kwargs.pop('edit_mode', False)
        super(ProductForm, self).__init__(*args, **kwargs)
        
        if is_edit_mode:
            for field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True  
class ProductNameForm(forms.ModelForm):
    class Meta:
        model = ProductName
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        edit_mode = kwargs.pop('edit_mode', False)
        super(IssuanceForm, self).__init__(*args, **kwargs)
        
        if edit_mode:
            for field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True   


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class ReorderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','reorder_level']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True