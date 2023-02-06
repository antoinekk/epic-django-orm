from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
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
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Client(models.Model):
    company = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='signed')
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={"team":"SALES"})

    def __str__(self):
        return self.email

class Contract(models.Model):
    reference = models.CharField(max_length=25, unique=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='signed')
    client_contact = models.ForeignKey(to=Client, on_delete=models.SET_NULL, null=True, limit_choices_to={"status": True})
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={"team":"SALES"})

    def __str__(self):
        return self.reference

class Event(models.Model):
    reference = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField(blank=True, auto_now_add=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='completed')
    contract = models.ForeignKey(to=Contract, on_delete=models.SET_NULL, null=True, limit_choices_to={"status": True})
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={"team":"SUPPORT"})

    def __str__(self):
        return self.reference
