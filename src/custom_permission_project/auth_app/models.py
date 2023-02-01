from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'ADMIN'),
        ('USER', 'USER')
    )
    role = models.CharField(max_length=20, choices=ROLES, default='USER')
    
