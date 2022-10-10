from rest_framework import serializers, status

from call.models import Call
from .models import Client, Number, Address
from call.serializer import CallSerializer


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'


class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    numbers = NumberSerializer(many=True, read_only=True)
    addresses = AddresSerializer(many=True, read_only=True)
    calls = CallSerializer(many=True, read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    name = serializers.CharField(read_only=False)

    class Meta:
        model = Client
        fields = '__all__'


class ClientPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    numbers = serializers.CharField(read_only=False)
    addresses = serializers.CharField(read_only=False)
    calls = CallSerializer(many=True, read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    name = serializers.CharField(read_only=False)

    class Meta:
        model = Client
        fields = '__all__'

# class ClientAllSerializer(serializers.ModelSerializer):
#     author = serializers.CharField(read_only=True)
#     numbers = NumberSerializer(many=False, read_only=True)
#     calls = serializers.CharField(read_only=False)
#     is_active = serializers.BooleanField(read_only=True)
#
#     class Meta:
#         model = Client
#         fields = '__all__'
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
