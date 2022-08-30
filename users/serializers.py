from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# from .authentication import generate_access_token
from .models import Permission, Role

User = get_user_model()

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Enter password', write_only=True, required=True, max_length=200)
    password_confirm = serializers.CharField(label='Repeat password', write_only=True, required=True, max_length=200)

    class Meta:
        model = User
        fields = [
            'id','first_name', 'last_name', 'username', 'email', 'password', 'password_confirm', 'role',
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
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]

    def validate(self, data):
        username = data['username']
        password = data['password']

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # user = User.objects.filter(username=username).first()
        #
        # if user is None:
        #     raise ValidationError('User not found!')
        #
        # if not user.check_password(password):
        #     raise ValidationError('Incorrect Password!')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A username or password was incorrect.'
            )


        # token = generate_access_token(user)
        # data['token'] = token
        return data


class UserSerializer(serializers.ModelSerializer):
    role = RoleRelatedField(many=False, queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
