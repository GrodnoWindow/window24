from rest_framework import serializers
from .models import Call
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# from client.serializer import ClientSerializer


class CallSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(read_only=True)

    class Meta:
        model = Call
        fields = '__all__'
