from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        if user.team == 'MANAGEMENT':
            user.is_superuser = True
        user.save()
        return user

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
    
    def change_status(self):
        if self.status == True:
            self.status.verbose_name = 'signed client'
        else:
            self.status.verbose_name = 'prospect'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
    
    def change_status(self):
        if self.status == True:
            self.status.verbose_name = 'signed'
        else:
            self.status.verbose_name = 'unsigned'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
    
    def change_status(self):
        if self.status == True:
            self.status.verbose_name = 'completed'
        else:
            self.status.verbose_name = 'uncompleted'