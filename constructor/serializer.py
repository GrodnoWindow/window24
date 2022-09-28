from rest_framework import serializers
from .models import *


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = '__all__'


class FittingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fittings
        fields = '__all__'


class SealOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealOutside
        fields = '__all__'


class SealRebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealRebate
        fields = '__all__'


class SealInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealInternal
        fields = '__all__'


class SealColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealColor
        fields = '__all__'


class ShprosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpros
        fields = '__all__'


class ShtapikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shtapik
        fields = '__all__'


class SashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sash
        fields = '__all__'


class LaminationOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination_outside
        fields = '__all__'


class LaminationInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination_inside
        fields = '__all__'


class ProfileWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_weight
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class ProductsInstallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_install
        fields = '__all__'


class PvcSlopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pvc_slopes
        fields = '__all__'


class FreePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Free_positions
        fields = '__all__'


class FavoritePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_positions
        fields = '__all__'


class WindowsillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill
        fields = '__all__'


class WindowsillDankeKomfortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill_danke_komfort
        fields = '__all__'


class WindowsillDankeStandartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill_danke_standart
        fields = '__all__'


class WindowsillDankePremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill_danke_premium
        fields = '__all__'


class LowTidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Low_tides
        fields = '__all__'


class VisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visors
        fields = '__all__'


class FlashingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashing
        fields = '__all__'


class FlashingMetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashing_metal
        fields = '__all__'


class PlatbandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platband
        fields = '__all__'


class ExtensionsToProfile60Serializer(serializers.ModelSerializer):
    class Meta:
        model = Extensions_to_profile_sixty
        fields = '__all__'


class ExtensionsToProfile70Serializer(serializers.ModelSerializer):
    class Meta:
        model = Extensions_to_profile_seventy
        fields = '__all__'


class BayWindowToProfile60Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bay_window_to_profile_sixty
        fields = '__all__'


class BayWindowToProfile70Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bay_window_to_profile_seventy
        fields = '__all__'


class Connector90gSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector_90g
        fields = '__all__'


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'


class HandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handles
        fields = '__all__'


class LocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locks
        fields = '__all__'


class StraightConnectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Straight_connectors
        fields = '__all__'


class SupplyValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_valve
        fields = '__all__'


class ConstructorSerializer(serializers.ModelSerializer):
    price = PriceSerializer(many=True, allow_null=True)
    product_type = ProductTypeSerializer(many=True, allow_null=True)
    profile = ProfileSerializer(many=True, allow_null=True)
    aggregate = AggregateSerializer(many=True, allow_null=True)
    fittings = FittingsSerializer(many=True, allow_null=True)
    seal_outside = SealOutsideSerializer(many=True, allow_null=True)
    seal_rebate = SealRebateSerializer(many=True, allow_null=True)
    seal_internal = SealInternalSerializer(many=True, allow_null=True)
    seal_color = SealColorSerializer(many=True, allow_null=True)
    shpros = ShprosSerializer(many=True, allow_null=True)
    shtapik = ShtapikSerializer(many=True, allow_null=True)
    sash = SashSerializer(many=True, allow_null=True)
    lamination_outside = LaminationOutsideSerializer(many=True, allow_null=True)
    lamination_inside = LaminationInsideSerializer(many=True, allow_null=True)
    profile_weight = ProfileWeightSerializer(many=True, allow_null=True)
    note = NoteSerializer(many=True, allow_null=True)
    products_install = ProductsInstallSerializer(many=True, allow_null=True)
    pvc_slopes = PvcSlopesSerializer(many=True, allow_null=True)
    free_positions = FreePositionsSerializer(many=True, allow_null=True)
    favorite_positions = FavoritePositionsSerializer(many=True, allow_null=True)
    windowsill = WindowsillSerializer(many=True, allow_null=True)
    windowsill_danke_komfort = WindowsillDankeKomfortSerializer(many=True, allow_null=True)
    windowsill_danke_standart = WindowsillDankeStandartSerializer(many=True, allow_null=True)
    windowsill_danke_premium = WindowsillDankePremiumSerializer(many=True, allow_null=True)
    low_tides = LowTidesSerializer(many=True, allow_null=True)
    visors = VisorsSerializer(many=True, allow_null=True)
    flashing = FlashingSerializer(many=True, allow_null=True)
    flashing_metal = FlashingMetalSerializer(many=True, allow_null=True)
    platband = PlatbandSerializer(many=True, allow_null=True)
    extensions_to_profile60 = ExtensionsToProfile60Serializer(many=True, allow_null=True)
    extensions_to_profile70 = ExtensionsToProfile70Serializer(many=True, allow_null=True)
    bay_window_to_profile60 = BayWindowToProfile60Serializer(many=True, allow_null=True)
    bay_window_to_profile70 = BayWindowToProfile70Serializer(many=True, allow_null=True)
    connector_90g = Connector90gSerializer(many=True, allow_null=True)
    accessories = AccessoriesSerializer(many=True, allow_null=True)
    handles = HandlesSerializer(many=True, allow_null=True)
    locks = LocksSerializer(many=True, allow_null=True)
    straight_connectors = StraightConnectorsSerializer(many=True, allow_null=True)
    supply_valve = SupplyValveSerializer(many=True, allow_null=True)

    class Meta:
        model = Constructor
        fields = '__all__'
