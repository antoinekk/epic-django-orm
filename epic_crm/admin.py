from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .models import User, Client, Contract, Event

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name', 'last_name', 'team', 'phone',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'team', 'phone',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    list_display = ('email', 'first_name', 'last_name', 'team', 'is_staff', 'is_superuser',)
    list_filter = ('team',)
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'company', 'phone', 'status', 'sales_contact',)}),
    )
    list_display = ('first_name', 'last_name', 'email', 'company', 'phone', 'status', 'sales_contact',)
    list_filter = ('company', 'sales_contact',)
    search_fields = ('company', 'sales_contact',)
    ordering = ('company', 'last_name')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('reference', 'amount', 'balance', 'status', 'client_contact', 'sales_contact',)}),
    )
    list_display = ('reference', 'amount', 'balance', 'creation_date', 'last_update', 'status', 'client_contact', 'sales_contact',)
    list_filter = ('client_contact', 'sales_contact',)
    search_fields = ('client_contact', 'sales_contact',)
    ordering = ('client_contact',)
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('reference', 'name', 'location', 'status', 'contract', 'support_contact',)}),
    )
    list_display = ('reference', 'name', 'location', 'creation_date', 'last_update', 'status', 'contract', 'support_contact',)
    list_filter = ('contract', 'support_contact',)
    search_fields = ('contract', 'support_contact',)
    ordering = ('contract',)

