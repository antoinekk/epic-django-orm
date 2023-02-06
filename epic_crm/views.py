from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from.permissions import *
from .serializers import *
from .models import *
from .filters import *

class SignupViewset(ModelViewSet):
    serializer_class = SignUpSerializer

    def get_queryset(self):
        return User.objects.all()

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & UserPermissions]

    def get_queryset(self):
        return User.objects.all()

class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated & ClientPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter

    def get_queryset(self):
        return Client.objects.all()

class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated & ContractPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContractFilter

    def get_queryset(self):
        return Contract.objects.all()

class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated & EventPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    
    def get_queryset(self):
        return Event.objects.all()