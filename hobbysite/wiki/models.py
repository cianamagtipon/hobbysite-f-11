from django.db import models
from django.contrib.auth.models import User

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__ (self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.title
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
