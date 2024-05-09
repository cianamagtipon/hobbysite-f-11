from django import forms
from .models import Product, Transaction

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].disabled = True

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        stock = cleaned_data.get('stock')
        if stock == 0:
            cleaned_data['status'] = 'Out of stock'
        else:
            cleaned_data['status'] = 'Available'
        return cleaned_data
    
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'status']