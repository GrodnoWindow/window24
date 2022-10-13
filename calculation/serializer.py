from rest_framework import serializers
from .models import WindowDiscount, WindowsillCalc, Order
from constructor.models import Constructor
from constructor.serializer import ConstructorSerializer


class WindowsillCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillCalc
        fields = '__all__'


class WindowsDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowDiscount
        fields = '__all__'


class WindowCalcSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
