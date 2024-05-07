from django.urls import path
from .views import index, ThreadListView, ThreadDetailView, ThreadCreateView

urlpatterns=[
    path('', index, name='index'),
    path('thread/add', ThreadCreateView.as_view()),
    path('threads/', ThreadListView.as_view(), name='threads'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread-detail')
]

app_name='forum'