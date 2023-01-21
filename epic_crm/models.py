from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class User(AbstractUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    teams = [
        ('SUPPORT', 'SUPPORT'),
        ('MANAGEMENT', 'MANAGEMENT'),
        ('SALES', 'SALES')
    ]
    team = models.CharField(choices=teams, max_length=10)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Client(models.Model):
    company = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='prospect')
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class Contract(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='unsigned')
    client_contact = models.ForeignKey(to=Client, on_delete=models.SET_NULL, null=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='uncompleted')
    contract = models.ForeignKey(to=Contract, on_delete=models.SET_NULL, null=True)
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
