from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

#
# class PermissionRelatedField(serializers.StringRelatedField):
#     def to_representation(self, value):
#         return PermissionSerializer(value).data
#
#     def to_internal_value(self, data):
#         return data