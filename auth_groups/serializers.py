from rest_framework import serializers
from django.contrib.auth.models import Group
from auth_permissions.serializers import PermissionSerializer


# Query creation for groups
class GroupSerializer(serializers.ModelSerializer):
    # permissions = PermissionRelatedField(many=True)
    # permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'
    #
    # def create(self, validated_data):
    #     permissions = validated_data.pop('permissions', None)
    #     instance = self.Meta.model(**validated_data)
    #     instance.save()
    #     instance.permissions.add(*permissions)
    #     instance.save()
    #     return instance


# class CreateGroupSerializer(serializers.ModelSerializer):
#     permissions = PermissionSerializer(many=True, read_only=True)
#     permission_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Permission.objects.all())
#
#     class Meta:
#         model = Group
#         fields = ('id', 'name', 'permissions', 'permission_ids',)
#
#     def create(self, validated_data):
#         permission_ids = validated_data.pop('permission_ids')
#         group = Group.objects.create(**validated_data)
#         group.permissions.set(permission_ids)
#         return group
#
#
# class GroupRelatedField(serializers.RelatedField):
#     def to_representation(self, instance):
#         return GroupSerializer(instance).data
#
#     def to_internal_value(self, data):
#         return self.queryset.get(pk=data)
