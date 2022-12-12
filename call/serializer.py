from rest_framework import serializers
from .models import Call

# from client.serializer import ClientSerializer


class CallSerializer(serializers.ModelSerializer):
    # id_client = ClientSerializer(read_only=True)

    class Meta:
        model = Call
        fields = '__all__'
