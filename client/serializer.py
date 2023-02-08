from rest_framework import serializers, status

from call.models import Call
from .models import Client, Number, Address, Prompter
from call.serializer import CallSerializer
from miscalculation.serializer import MiscalculationSerializer
from complaint.serializer import ComplaintSerializer


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['id', 'number', 'name']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name']


class PrompterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompter
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=False)
    is_active = serializers.BooleanField(read_only=True)
    numbers = NumberSerializer(many=True, read_only=False)
    addresses = AddressSerializer(many=True, read_only=False)
    prompter = PrompterSerializer(many=True, read_only=False)
    calls = CallSerializer(many=True, read_only=False)
    miscalculation = MiscalculationSerializer(many=True, read_only=False)
    complaints = ComplaintSerializer(many=True, read_only=False)
    category_select = serializers.IntegerField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientPostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=False)
    is_active = serializers.BooleanField(read_only=True)
    author = serializers.CharField(read_only=True)
    calls = CallSerializer(many=True, read_only=True)
    numbers = NumberSerializer(many=True, read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)
    prompter = PrompterSerializer(many=True, read_only=True)
    miscalculation = MiscalculationSerializer(many=True, read_only=True)
    complaints = ComplaintSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
