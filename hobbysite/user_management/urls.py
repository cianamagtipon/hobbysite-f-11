from django.urls import path
from .views import UpdateView

urlpatterns=[
    path('profile', UpdateView.as_view(), name='profile'),
]

app_name='user_management'