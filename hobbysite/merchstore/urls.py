from django.urls import path
from .views import (
    ProductTypeView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    CartView,
    TransactionListView,
)

urlpatterns = [
    path('items/', ProductTypeView.as_view(), name='list'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('item/add/', ProductCreateView.as_view(), name='create'),
    path('item/<int:pk>/edit/', ProductUpdateView.as_view(), name='update'),
    path('cart/', CartView.as_view(), name='cart'),
    path('transactions/', TransactionListView.as_view(), name='transactions'),
]

app_name = "merchstore"
