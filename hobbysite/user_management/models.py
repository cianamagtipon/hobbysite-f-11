from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField()
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user_management:profile')