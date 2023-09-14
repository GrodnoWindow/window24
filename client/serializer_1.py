from rest_framework import serializers
from .models import Client, Number, Address, Prompter, Contract, PassportDetails


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['__all__']


class PassportDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportDetails
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name']


class PrompterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompter
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
