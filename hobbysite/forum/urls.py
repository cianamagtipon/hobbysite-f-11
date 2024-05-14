from django.urls import path
from .views import index, ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView

app_name = 'forum'

urlpatterns = [ 
    path('threads/', ThreadListView.as_view(), name='threads'),  # List view
    path('thread/add', ThreadCreateView.as_view(), name='thread-add'),  # Create view
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),  # Detail view
    path('thread/<int:pk>/edit', ThreadUpdateView.as_view(), name='thread-edit'),  # Edit view
]
