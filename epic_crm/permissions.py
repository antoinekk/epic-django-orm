from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import *

class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'DELETE']:
            return request.user.team == 'MANAGEMENT'
        return True

class ClientPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in 'POST':
            return request.user.team in ('MANAGEMENT', 'SALES')
        if request.method in ['PUT', 'DELETE']:
            return request.user == obj.sales_contact
        return True

class ContractPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in 'POST':
            client_id = view.kwargs.get('client_id')
            client = Client.objects.get(id=client_id)
            if client.sales_contact != request.user:
                return False
        elif request.method in ['PUT', 'DELETE']:
            return request.user == obj.sales_contact
        return True

class EventPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in 'POST':
            contract_id = view.kwargs.get('contract_id')
            contract = Contract.objects.get(id=contract_id)
            if contract.support_contact != request.user:
                return False
        elif request.method in ['PUT', 'DELETE']:
            return request.user == obj.support_contact
        return True
    
