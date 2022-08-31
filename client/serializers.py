from rest_framework import serializers
from .models import Client
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class CLientModel:
#     def __init__(self,name):
#         self.name = name


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    # author = serializers.CharField(max_length=255)
    # name = serializers.CharField(max_length=255)

    # def create(self, validated_data):
    #     return Client.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name",instance.name)
    #
    #     instance.save()
    #     return instance

# def encode():
#     model = CLientModel('angelina jolie')
#     model_sr = ClientSerializer(model)
#     print(model_sr.data, type(model_sr.data),type(model_sr), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO('')
#     data = JSONParser().parse(stream)
#     serializers = ClientSerializer(data)
#     serializers.is_valid() # check valid data
#     print(serializers.validated_data)