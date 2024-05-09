from django.urls import path
from .views import ProfileUpdateView, register

app_name = 'user_management'
urlpatterns = [
    path('profile/update', ProfileUpdateView.as_view(), name='update_profile'),
    path('register/', register, name='register'),  # New registration path
]
