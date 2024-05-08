from django.urls import path
from . import views

app_name = 'commissions'

urlpatterns = [
    path('list/', views.commission_list, name='commission_list'),
    path('detail/<int:pk>/', views.commission_detail, name='commission_detail'),
    path('add/', views.commission_create, name='commission_add'),  # Ensure the view and name match your actual implementation
    path('edit/<int:pk>/', views.commission_update, name='commission_edit'),
]
