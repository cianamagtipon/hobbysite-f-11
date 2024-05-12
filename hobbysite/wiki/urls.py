from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns=[
    path('', ArticleListView.as_view(), name='index'),
    path('article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail')
]

app_name='wiki'
