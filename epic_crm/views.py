from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from.permissions import *
from .serializers import *
from .models import *

class SignupView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ClientView(APIView):

    permission_classes = [IsAuthenticated & ClientPermissions]

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

class ClientDetailsView(APIView):

    permission_classes = [IsAuthenticated & ClientPermissions]
    
    def get(self, request, id):
        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
    def put(self, request, id):
        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        client = Client.objects.get(id=id)
        client.delete()
        return Response('Client has been deleted')

class ContractView(APIView):

    permission_classes = [IsAuthenticated & ContractPermissions]

    def post(self, request, id):
        client = Client.objects.get(id=id)
        request.data['client_contact'] = client.id
        serializer = ContractSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request, id):
        client = Client.objects.get(id=id)
        contracts = Contract.objects.filter(client_contact=client)
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)

class ContractDetailsView(APIView):

    permission_classes = [IsAuthenticated & ContractPermissions]

    def get(self, request, id):
        contract = Contract.objects.get(id=id)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    
    def put(self, request, id):
        contract = Contract.objects.get(id=id)
        request.data['client_contact'] = contract.client_contact.id
        serializer = ContractSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        contract = Contract.objects.get(id=id)
        contract.delete()
        return Reponse('Contract has been deleted')


class EventView(APIView):

    permission_classes = [IsAuthenticated & EventPermissions]

    def post(self, request, id):
        contract = Contract.objects.get(id=id)
        request.data['contract'] = contract.id
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
    def get(self, request, id):
        contract = Contract.objects.get(id=id)
        events = Event.objects.filter(contract=contract)
        serializer = ContractSerializer(events, many=True)
        return Response(serializer.data)

class EventDetailsView(APIView):

    permission_classes = [IsAuthenticated & EventPermissions]

    def get(self, request, event_id):
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, event_id):
        event = Contract.objects.get(id=id)
        request.data['contract'] = event.contract.id
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        event = Event.objects.get(id=id)
        event.delete()
        return Reponse('Event has been deleted')