from rest_framework import serializers
from .models import Call
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class CLientModel:
#     def __init__(self,name):
#         self.name = name


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'
