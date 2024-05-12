from django.urls import path
from .views import index, ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView

urlpatterns=[
    path('', index, name='index'),
    path('thread/add', ThreadCreateView.as_view(), name='thread-add'),
    path('thread/<int:pk>/edit', ThreadUpdateView.as_view(), name='thread-edit'),
    path('threads/', ThreadListView.as_view(), name='threads'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread-detail')
]

app_name='forum'