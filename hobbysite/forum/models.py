from django.db import models
from django.urls import reverse
from django.conf import settings

class ThreadCategory(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Thread Category"
        verbose_name_plural = "Thread Categories"

class Thread(models.Model):
    title = models.CharField(max_length=225)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='forum_threads', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(ThreadCategory, related_name='threads', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_root_url(self):
        return reverse('forum:threads')

    def get_absolute_url(self):
        return reverse('forum:thread-detail', args=[self.pk])
    
    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Thread"
        verbose_name_plural = "Threads"

class Comment(models.Model):
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='forum_comments', on_delete=models.SET_NULL, null=True, blank=True)
    thread = models.ForeignKey(Thread, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.entry
    
    def get_root_url(self):
        return reverse('forum:threads')

    def get_absolute_url(self):
        return reverse('forum:thread-detail', args=[self.pk])
    
    class Meta:
        ordering = ["created_on"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
