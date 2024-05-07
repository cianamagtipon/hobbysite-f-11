from django.urls import path
from .views import index, UpdateView
from django.views.generic.edit import UpdateView

urlpatterns=[
    path('', index, name='index'),
    path('profile', UpdateView.as_view(), name='profile'),
]

app_name='user_management'