from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from user_management.views import register
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the user_management URLs. Consider if you need the empty path ('') for it.
    path('user_management/', include('user_management.urls', namespace="user_management")),
    
    # Other apps' URLs
    path('forum/', include('forum.urls', namespace='forum')),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('merchstore/', include('merchstore.urls', namespace="merchstore")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    
    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user_management/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path('accounts/register/', register, name='register'),

    # Homepage URL - Make sure this is not duplicated or conflicting.
    path('', views.homepage, name='homepage'),  # Home page route
]
