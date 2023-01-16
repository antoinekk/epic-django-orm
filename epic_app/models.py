from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    TEAMS = [
        ('SUPPORT', 'SUPPORT'),
        ('MANAGEMENT', 'MANAGEMENT'),
        ('SALES', 'SALES')
    ]
    team = models.CharField(choices=TEAMS, max_length=10)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Client(models.Model):
    company = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


