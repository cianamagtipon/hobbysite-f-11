from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
        widgets = {
            'owner': forms.HiddenInput(),
            'product_type': forms.Select(),
            'status': forms.Select(choices=Product.STATUS_CHOICES),
        }

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'description', 'price', 'stock']
        widgets = {
            'owner': forms.HiddenInput(),
            'product_type': forms.Select(),
        }

    def clean(self):
        cleaned_data = super().clean()
        stock = cleaned_data.get('stock')
        if stock == 0:
            cleaned_data['status'] = 'Out of stock'
        else:
            cleaned_data['status'] = 'Available'
        return cleaned_data
