from rest_framework import serializers
from .models import WindowDiscount, WindowsillCalc, Order, WindowsillCalc
from constructor.models import Constructor
from constructor.serializer import ConstructorSerializer


class WindowsCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowDiscount
        fields = 'profile_id', 'fittings_id'


class WindowsillCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillCalc
        fields = '__all__'


class ConstructorCalcSerializer(serializers.ModelSerializer):
    visors = serializers.CharField(read_only=False)
    width_windowsill = serializers.SerializerMethodField('get_width_windowsill')
    window = WindowsCalcSerializer(read_only=False)
    profile = serializers.CharField(read_only=True)
    windowsill = WindowsillCalcSerializer(many=True,read_only=False)

    def get_width_windowsill(self, foo):
        return "0"

    class Meta:
        model = Constructor
        fields = '__all__'
