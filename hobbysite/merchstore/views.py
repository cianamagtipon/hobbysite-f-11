from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from user_management.models import Profile
from .forms import ProductCreateForm, ProductUpdateForm, TransactionForm
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


class ProductTypeView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.exclude(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_products = Product.objects.filter(owner=self.request.user)
            context['user_products'] = user_products
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        related_products = product.product_type.products.all()
        context['related_products'] = related_products
        context['transaction_form'] = TransactionForm()
        context['can_edit'] = self.request.user == product.owner
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TransactionForm(request.POST)
        if form.is_valid():
            product = self.object
            quantity = form.cleaned_data['amount']
            if product.stock >= quantity:
                if request.user == product.owner:  # Check if current user is the owner
                    return HttpResponseForbidden("You cannot buy your own product.")
                product.stock -= quantity
                product.save()
                if request.user.is_authenticated:
                    transaction = form.save(commit=False)
                    transaction.product = product
                    transaction.buyer = request.user
                    transaction.save()
                    return redirect('merchstore:cart')
                else:
                    return redirect('login')
            else:
                pass
        return self.render_to_response(self.get_context_data(form=form))


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'product_create.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial

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
            return HttpResponseForbidden("You don't own this.")
        if not self.test_func() and not request.user.is_superuser:
            return HttpResponseForbidden("You don't own this.")
        return super().dispatch(request, *args, **kwargs)


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        purchased = Transaction.objects.filter(buyer=self.request.user)
        ctx['purchased_items'] = purchased
        return ctx


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        items_sold = Product.objects.filter(owner=self.request.user)
        transactions = Transaction.objects.filter(product__in=items_sold)
        ctx['all_transactions'] = transactions
        return ctx
