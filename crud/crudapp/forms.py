from django import forms
from .models import Item, Vendedor

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor  
        fields = ['nombre', 'apellido']     
        