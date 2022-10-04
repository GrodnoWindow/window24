from rest_framework import serializers, status
from .models import Client, Number
from call.serializer import CallSerializer


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    number = serializers.CharField(read_only=False)
    calls = CallSerializer(many=True, read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientAllSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    number = NumberSerializer(many=True, read_only=True)
    calls = CallSerializer(many=True, read_only=True)
    is_active = serializers.BooleanField(read_only=True)

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
