from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('articles/', views.article_list_view, name='article-list'),
    #path('article/<int:pk>/', views.article_detail_view, name='article-detail'),
    #path('article/create/', views.article_create_view)
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article-update'),
]

