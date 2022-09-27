from rest_framework import serializers
from .models import Constructor


class ConstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Constructor
        fields = '__all__'
