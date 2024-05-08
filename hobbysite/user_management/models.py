from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Profile(AbstractUser):
    display_name = models.CharField(max_length=63, blank=True, verbose_name="Display Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="profile_set",  # Unique related_name for Profile
        related_query_name="profile",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="profile_perm_set",  # Unique related_name for Profile
        related_query_name="profile",
    )

    def __str__(self):
        return f"{self.display_name} ({self.username})" if self.display_name else self.username
