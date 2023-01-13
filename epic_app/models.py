from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    TEAMS = [
        ('SUPPORT', 'SUPPORT'),
        ('MANAGEMENT', 'MANAGEMENT'),
        ('SALES', 'SALES')
    ]
    team = models.CharField(choices=TEAMS, max_length=10)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
