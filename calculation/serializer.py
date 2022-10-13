from rest_framework import serializers
from .models import WindowDiscount
from constructor.models import Constructor


class ConstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Constructor
        fields = '__all__'


class WindowsDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowDiscount
        fields = '__all__'
