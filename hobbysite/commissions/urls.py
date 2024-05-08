from django.urls import path
from . import views

app_name = 'commissions'

urlpatterns = [
    path('list/', views.commission_list, name='commission_list'),  # Ensure trailing slashes
    path('detail/<int:pk>/', views.commission_detail, name='commission_detail'),
]
