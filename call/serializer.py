from rest_framework import serializers
from .models import Call

# from client.serializer import ClientSerializer


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'
