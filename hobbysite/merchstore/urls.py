from django.urls import path
from .views import ProductTypeView, ProductDetailView

urlpatterns = [
    path('items/', ProductTypeView.as_view(), name='list'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='detail')
]

app_name = "merchstore"