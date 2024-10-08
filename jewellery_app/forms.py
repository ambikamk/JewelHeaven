from django import forms
from .models import Product

from .models import Address

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock','image','description','base_metal','stone_type','sizing','type','plating','country_of_origin']
        
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image','description','base_metal','stone_type','sizing','type','plating','country_of_origin']
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['recepient_name', 'recepient_contact', 'address_line1', 'address_line2', 'city', 'state', 'postal_code']
        widgets = {
            'recepient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipient Name'}),
            'recepient_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipient Contact'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
        }