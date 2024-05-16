from django.db import models
from django.conf import settings

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wiki_articles', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, related_name='articles', on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    header_image = models.ImageField(upload_to='articles/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wiki_comments', on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
