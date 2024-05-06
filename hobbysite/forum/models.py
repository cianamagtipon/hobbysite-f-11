from django.db import models
from django.urls import reverse

from time import timezone
import datetime


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
    # (optional) image
    # author
    category = models.ForeignKey(
        ThreadCategory, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='threads'
    )
    
    def __str__(self):
        return self.title
    
    def get_root_url(self):
        return reverse('forum:threads')

    def get_absolute_url(self):
        return reverse('forum:forum-detail', args=[self.pk])
    
    
    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Thread"
        verbose_name_plural = "Threads"