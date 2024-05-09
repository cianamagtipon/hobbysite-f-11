from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls', namespace='forum')),
    path('wiki/', include('wiki.urls', namespace='wiki')),
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
    path('commissions/', include('commissions.urls', namespace='commissions')),
    path('user_management/', include('user_management.urls', namespace='user_management')),  # Includes user_management with its dedicated namespace
    path('', views.homepage, name='homepage'),  # Home page route
    path('accounts/', include('django.contrib.auth.urls')),  # Django built-in authentication URLs
]
