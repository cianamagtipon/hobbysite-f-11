from django.urls import path
from .views import UpdateView
from .views import register

urlpatterns=[
    path('profile', UpdateView.as_view(), name='profile'),
    path('register/', register, name='register')
]

app_name='user_management'