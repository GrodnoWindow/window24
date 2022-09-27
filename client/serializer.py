from datetime import datetime

from requests import Response
from rest_framework import serializers, status
from .models import Client
from call.serializer import CallSerializer
from .models import Call
from django.db import models


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    number = serializers.CharField(read_only=False)
    calls = CallSerializer(many=True,read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

    # def create(self, validated_data):
    #     # create market data for Market model.
    #     # call = Call.objects.filter(id=validated_data['calls'])
    #
    #
    #     client = Client.objects.create(
    #         name=validated_data['name'],
    #         author=validated_data['author'],
    #     )
    #     client.calls.add(1)
    #     client.number.add(1)
    #
    #     return {'asd':'asdasd'}
