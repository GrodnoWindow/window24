from rest_framework import serializers
from .models import *
from call.serializer import CallSerializer
from client.serializer import ClientSerializer


class CallsTableSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=False)
    call = CallSerializer(many=False, read_only=False)

    class Meta:
        model = CallsTable
        fields = '__all__'


class OutGoingCallSerializer(serializers.ModelSerializer):


    class Meta:
        model = OutgoingCalls
        fields = '__all__'