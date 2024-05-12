from django.urls import path
from . import views
from .views import ArticleForm

urlpatterns = [
    path('articles/', views.article_list_view, name='article-list'),
    path('article/<int:pk>/', views.article_detail_view, name='article-detail'),
    path('article/create/', views.article_create_view, name='article-create'),
    path('article/<int:pk>/update/', views.article_update_view, name='article-update'),
]

app_name = 'wiki'
