from django.urls import path
from . import views

urlpatterns = [
    path('list', views.commission_list, name='commission_list'),
    path('detail/<int:pk>', views.commission_detail, name='commission_detail'),
]

app_name='commissions'