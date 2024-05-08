from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from user_management.models import Profile


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

        related_products = self.object.product_type.products.all()
        context['related_products'] = related_products
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.instance.stock == 0:
            form.instance.status = 'Out of stock'
        else:
            form.instance.status = 'Available'
        return super().form_valid(form)


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'cart.html'
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        items_bought = Product.objects.filter(owner=user)
        ctx['bought'] = items_bought
        return ctx


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        items_sold = Product.objects.filter(owner=user)
        ctx['sold'] = items_sold
        return ctx
