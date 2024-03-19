from django.contrib import admin
from django.urls import path, include

urlpatterns=[
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls', namespace="forum")),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('merchstore/items/', ProductTypeView.as_view(), name='list'),
    path('merchstore/item/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('merchstore/', include('merchstore.urls', namespace='merchstore'))
]