from rest_framework import serializers
from .models import WindowDiscount


class WindowsDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowDiscount
        fields = '__all__'