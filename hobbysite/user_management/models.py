from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    display_name = models.CharField(max_length=63, blank=True, verbose_name="Display Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")

    def __str__(self):
        return f"{self.display_name} ({self.username})" if self.display_name else self.username
