from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Profile(AbstractUser):
    display_name = models.CharField(max_length=63)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('user_management:profile_detail')
