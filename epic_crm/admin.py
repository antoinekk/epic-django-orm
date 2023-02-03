from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User, Client, Contract, Event
from django.contrib.auth.models import Group

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name', 'last_name', 'team', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'team', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    list_display = ('email', 'first_name', 'last_name', 'team', 'is_staff', 'is_superuser',)
    list_filter = ('team',)
    ordering = ('email',)

    def has_view_permission(self, request, obj=None):
        return request.user.team == 'MANAGEMENT'

    def has_add_permission(self, request, obj=None):
        return request.user.team == 'MANAGEMENT'

    def has_change_permission(self, request, obj=None):
        return request.user.team == 'MANAGEMENT'

    def has_delete_permission(self, request, obj=None):
        return request.user.team == 'MANAGEMENT'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'company', 'phone', 'status', 'sales_contact',)}),
    )
    list_display = ('first_name', 'last_name', 'email', 'company', 'phone', 'status', 'sales_contact',)
    list_filter = ('sales_contact',)
    ordering = ('company',)

    def has_view_permission(self, request, obj=None):
        return super().has_view_permission(request, obj)

    def has_add_permission(self, request, obj=None):
        return request.user.team in ('MANAGEMENT', 'SALES')

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.sales_contact == request.user or request.user.team == 'MANAGEMENT'
            
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        if obj.status == False:
            return obj.sales_contact == request.user or request.user.team == 'MANAGEMENT'

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('reference', 'amount', 'balance', 'status', 'client_contact', 'sales_contact',)}),
    )
    list_display = ('reference', 'amount', 'balance', 'creation_date', 'last_update', 'status', 'client_contact', 'sales_contact',)
    list_filter = ('client_contact', 'sales_contact',)
    ordering = ('client_contact',)

    def has_view_permission(self, request, obj=None):
        return super().has_view_permission(request, obj)
    
    def has_add_permission(self, request, obj=None):
        return request.user.team in ('MANAGEMENT', 'SALES')

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.sales_contact == request.user or request.user.team == 'MANAGEMENT'
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        if obj.status == False:
            return obj.sales_contact == request.user or request.user.team == 'MANAGEMENT'
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('reference', 'name', 'location', 'status', 'contract', 'support_contact',)}),
    )
    list_display = ('reference', 'name', 'location', 'creation_date', 'last_update', 'status', 'contract', 'support_contact',)
    list_filter = ('contract', 'support_contact',)
    ordering = ('contract',)

    def has_view_permission(self, request, obj=None):
        return super().has_view_permission(request, obj)
    
    def has_add_permission(self, request, obj=None):
        return request.user.team in ('MANAGEMENT', 'SALES')
    
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.support_contact == request.user or request.user.team == 'MANAGEMENT'
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        if obj.status == False:
            return obj.support_contact == request.user or request.user.team == 'MANAGEMENT'

admin.site.unregister(Group)