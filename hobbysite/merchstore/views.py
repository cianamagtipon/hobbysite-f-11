from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductTypeView(ListView):
    model = Product
    template_name = 'product_type.html'
    context_object_name = 'product'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Access related products through the reverse relationship
        related_products = self.object.product_type.products.all()
        context['related_products'] = related_products
        return context
