from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from user_management.views import register
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='user_management/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path('register/', register, name='register'),
    path('user_management/', include('user_management.urls', namespace='user_management')),
    path('commissions/', include('commissions.urls', namespace='commissions')),
    path('', views.homepage, name='homepage'),  # Home page route
]
