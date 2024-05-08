from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name='article-list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article-update'),
]
]
