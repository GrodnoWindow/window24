from rest_framework import serializers
from .models import *
from constructor.serializer import WorksSerializer


class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRates
        fields = '__all__'


class WindowSerializer(serializers.ModelSerializer):
    price_input = serializers.FloatField(max_value=None, min_value=None)
    currency_name = serializers.CharField(max_length=255, read_only=False)

    class Meta:
        model = WindowDiscountMarkups
        fields = 'profile_id', 'fittings_id', 'price_input', 'currency_name',


class WindowsillCalcSerializer(serializers.ModelSerializer):
    windowsill_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = WindowsillCalc
        fields = 'windowsill_id', 'width', 'length', 'count', 'markups_type'


class LowTidesCalcSerializer(serializers.ModelSerializer):
    low_tides_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = LowTidesCalc
        fields = 'low_tides_id', 'width', 'length', 'count', 'markups_type'


class WindowCalcSerializer(serializers.ModelSerializer):
    window = WindowSerializer(read_only=False)
    price_input = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    price_output = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    fittings_id = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    profile_id = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    discount = serializers.FloatField(read_only=True)
    currency_name = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    currency_value = serializers.FloatField(max_value=None, min_value=None, read_only=True)

    markup_value = serializers.FloatField(max_value=None, min_value=None, read_only=True)
    markup_percent = serializers.FloatField(max_value=None, min_value=None, read_only=True)

    class Meta:
        model = WindowsCalc
        fields = '__all__'


class ConstructorSerializer(serializers.ModelSerializer):
    # works = WorksSerializer(many=True, required=False)

    class Meta:
        model = Constructor
        fields = '__all__'


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'


class LaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination
        fields = '__all__'


class ConnectionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionProfile
        fields = '__all__'


class AdditionalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalProfile
        fields = '__all__'


class SealantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sealant
        fields = '__all__'
