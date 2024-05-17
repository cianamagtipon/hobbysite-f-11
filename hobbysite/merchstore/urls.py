from django.urls import path
from . import views

app_name = "merchstore"

urlpatterns = [
    path('items/', views.ProductTypeView.as_view(), name='list'),  # Make sure 'list' is what's used in templates
    path('item/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('item/add/', views.ProductCreateView.as_view(), name='create'),
    path('item/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='update'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('transactions/', views.TransactionListView.as_view(), name='transactions'),
]
