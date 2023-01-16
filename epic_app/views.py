from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

class SignupView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ClientView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.team == 'SALES':
            request.data['sales_contact'] = request.user.id
            serializer = ClientSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            client = serializer.save()
            return Response(serializer.data)
        else:
            return Response('Only sales team member can create a new client.')
    
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

class ClientDetailsView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
    def put(self, request, id):
        client = Client.objects.get(id=id)
        print(client.sales_contact.id)
        if request.user.id == client.sales_contact.id or request.user.team == 'MANAGEMENT':
            serializer = ClientSerializer(client, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Only sales team owner or management team can modify this client.')




