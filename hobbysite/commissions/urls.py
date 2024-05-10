from django.urls import path
from . import views

app_name = 'commissions'

urlpatterns = [
    path('list/', views.commission_list, name='list'),  # Renamed for consistency with the template call
    path('detail/<int:pk>/', views.commission_detail, name='detail'),
    path('add/', views.commission_create, name='add'),
    path('edit/<int:pk>/', views.commission_update, name='edit'),
]
