from rest_framework import serializers, status

from .models import *
from users.serializers import UserSerializer


class ComplaintSerializer(serializers.ModelSerializer):
    executor = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Complaint
        fields = '__all__'
