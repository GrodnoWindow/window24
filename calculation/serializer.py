from rest_framework import serializers
from .models import WindowDiscount, WindowsillCalc, WindowsillCalc
from constructor.models import Constructor
from constructor.serializer import ConstructorSerializer

from constructor.models import Windowsill


class WindowsillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill
        fields = 'id'


class WindowsCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowDiscount
        fields = 'profile_id', 'fitting_id'


class WindowsillCalcSerializer(serializers.ModelSerializer):
    windowsill = WindowsillSerializer(read_only=False, many=False)

    class Meta:
        model = WindowsillCalc
        fields = 'windowsill', 'width', 'length', 'count', 'price'


class ConstructorCalcSerializer(serializers.ModelSerializer):
    # window = WindowsCalcSerializer(read_only=False)
    #
    # windowsills = WindowsillCalcSerializer(many=True, read_only=False)
    # currency = serializers.SerializerMethodField('get_current_currency')

    # profile = serializers.CharField(read_only=True)
    # price_input = serializers.CharField(read_only=True)
    # price_output = serializers.CharField(read_only=True)
    # product_type = serializers.CharField(read_only=True)
    # profile = serializers.CharField(read_only=True)
    # aggregate = serializers.CharField(read_only=True)
    # fittings = serializers.CharField(read_only=True)
    # seal_outside = serializers.CharField(read_only=True)
    # seal_rebate = serializers.CharField(read_only=True)
    # seal_internal = serializers.CharField(read_only=True)
    # seal_color = serializers.CharField(read_only=True)
    # shpros = serializers.CharField(read_only=True)
    # shtapik = serializers.CharField(read_only=True)
    # sash = serializers.CharField(read_only=True)
    # lamination_outside = serializers.CharField(read_only=True)
    # lamination_inside = serializers.CharField(read_only=True)
    # profile_weight = serializers.CharField(read_only=True)
    # note = serializers.CharField(read_only=True)
    # products_install = serializers.CharField(read_only=True)
    # pvc_slopes = serializers.CharField(read_only=True)
    # free_positions = serializers.CharField(read_only=True)
    # favorite_positions = serializers.CharField(read_only=True)
    # windowsill = serializers.CharField(read_only=True)
    # visors = serializers.CharField(read_only=True)
    # flashing = serializers.CharField(read_only=True),
    # flashing_metal = serializers.CharField(read_only=True)
    # platband = serializers.CharField(read_only=True),
    # extensions_to_profile60 = serializers.CharField(read_only=True),
    # extensions_to_profile70 = serializers.CharField(read_only=True),
    # bay_window_to_profile60 = serializers.CharField(read_only=True)
    # bay_window_to_profile70 = serializers.CharField(read_only=True)
    # connector_90g = serializers.CharField(read_only=True)
    # accessories = serializers.CharField(read_only=True)
    # handles = serializers.CharField(read_only=True)
    # locks = serializers.CharField(read_only=True)
    # straight_connectors = serializers.CharField(read_only=True)
    # supply_valve = serializers.CharField(read_only=True)

    def get_current_currency(self, foo):
        return "RUB"

    class Meta:
        model = Constructor
        fields = '__all__'
