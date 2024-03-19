from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('articles/', views.article_list_view, name='article-list'),
    path('article/<int:pk>/', views.article_detail_view, name='article-detail'),
]
