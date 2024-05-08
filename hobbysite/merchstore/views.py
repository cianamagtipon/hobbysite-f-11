from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from user_management.models import Profile
from .forms import ProductCreateForm, ProductUpdateForm
from django.urls import reverse_lazy


class ProductTypeView(ListView):
    model = Product
    template_name = 'home.html'
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
    form_class = ProductCreateForm
    template_name = 'product_create.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('merchstore:list')

    def form_valid(self, form):
        form.instance.owner = self.object.owner
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not self.test_func() and not request.user.is_superuser:
            # Allow superusers to edit any product
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


    

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
