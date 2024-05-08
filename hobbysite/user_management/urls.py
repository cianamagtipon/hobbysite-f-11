from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('profile/', views.profile_update, name='profile_update'), 
]
