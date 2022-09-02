from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Permission, Group, ContentType

from auth_groups.serializers import GroupSerializer
from .models import User





# class ContentTypeSerializer(serializers.ModelSerializer):
#     permission = PermissionSerializer(many=True)
#
#     class Meta:
#         model = ContentType
#         fields = '__all__'




class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Enter password', write_only=True, required=True, max_length=200)
    password_confirm = serializers.CharField(label='Repeat password', write_only=True, required=True, max_length=200)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'password', 'password_confirm', 'group'
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'password_confirm': {'write_only': True},
        # }

    def validate_password2(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            msg = 'Passwords do not match!'
            raise ValidationError(msg)
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=True,
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    # group = GroupRelatedField(many=False, queryset=Group.objects.all())
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'password',
            'is_superuser', 'groups', 'user_permissions', 'is_active'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    #
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


class GetUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class GetGroupSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True)
    # permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
