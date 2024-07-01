from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='Society_Members',  # Change this
        blank=True,
        help_text=('Society member groups in this neighborhood.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='Guards',  # Change this
        blank=True,
        help_text=('Specific permissions for guards in the society.'),
        verbose_name=('user permissions'),
    )