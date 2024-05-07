from django.urls import path
from .views import index, ThreadListView, ThreadDetailView

urlpatterns=[
    path('', index, name='index'),
    path('threads/', ThreadListView.as_view(), name='threads'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='forum-detail')
]

app_name='forum'