# forum/urls.py
from django.urls import path
from .views import index, ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView

app_name = 'forum'

urlpatterns = [
    path('', ThreadListView.as_view(), name='threads'),  # Renamed from index to threads
    path('thread/add', ThreadCreateView.as_view(), name='thread-add'),
    path('thread/<int:pk>/edit', ThreadUpdateView.as_view(), name='thread-edit'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread-detail')
]
