from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)

app_name = 'wiki'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/add/', ArticleCreateView.as_view(), name='article-add'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),  # Correctly named here
]
