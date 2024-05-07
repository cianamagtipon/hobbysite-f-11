from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=63, verbose_name="Display Name")
    email_address = models.EmailField(verbose_name="Email Address")

    def __str__(self):
        return f"{self.display_name} ({self.user.username})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

