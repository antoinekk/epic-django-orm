from django_filters import rest_framework as filters
from .models import Client, Contract, Event


class ClientFilter(filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            'last_name': ['exact', 'icontains'],
            'email': ['exact', 'icontains']
        }

class ContractFilter(filters.FilterSet):
    class Meta:
        model = Contract
        fields = {
            'client_contact__last_name': ['exact', 'icontains'],
            'client_contact__email': ['exact', 'icontains'],
            'creation_date': ['exact', 'icontains', 'gte', 'lte'],
            'amount': ['exact', 'gte', 'lte']
        }

class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'contract__sales_contact__last_name': ['exact', 'icontains'],
            'contract__sales_contact__email': ['exact', 'icontains'],
            'event_date': ['exact', 'gte', 'lte']
        }