from django.urls import path
from .views import index, ThreadListView, ThreadDetailView, ThreadCreateView

urlpatterns=[
    path('', index, name='index'),
    path('threads/', ThreadListView.as_view(), name='threads'),
    path('create/', ThreadCreateView.as_view()),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread-detail')
]

app_name='forum'