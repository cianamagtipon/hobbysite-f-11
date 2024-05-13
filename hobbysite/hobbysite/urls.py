from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from user_management.views import register
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_management.urls', namespace="user_management")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('merchstore/', include('merchstore.urls', namespace="merchstore")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    path('', include('django.contrib.auth.urls')),
    # path('register/', register, name='register'),
    path('home/', views.homepage, name='homepage')
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user_management/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path('accounts/register/', register, name='register'),  # Optionally prefix with 'accounts/' for consistency
    path('user_management/', include('user_management.urls', namespace='user_management')),
    path('commissions/', include('commissions.urls', namespace='commissions')),
    path('', views.homepage, name='homepage'),  # Home page route
]
