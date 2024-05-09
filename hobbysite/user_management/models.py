from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Profile(AbstractUser):
    display_name = models.CharField(max_length=63, unique=True)
    email = models.EmailField(unique=True)  # Use the built-in email field and ensure it's unique

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('user_management:update_profile')  # Update the URL name based on your URL configuration
