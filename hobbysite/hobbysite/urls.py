from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', include('user_management.urls', namespace="user_management")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('merchstore/', include('merchstore.urls', namespace="merchstore")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    path('', include('django.contrib.auth.urls')),
    # path('register/', register, name='register'),
    path('home/', views.homepage, name='homepage')
]