from rest_framework import serializers
from .models import *


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    price = PriceSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'price']


class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = ['id', 'name']


class FittingsSerializer(serializers.ModelSerializer):
    price = PriceSerializer(many=True)

    class Meta:
        model = Fittings
        fields = ['id', 'name', 'price']


class SealOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealOutside
        fields = ['id', 'name']


class SealRebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealRebate
        fields = ['id', 'name']


class SealInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealInternal
        fields = ['id', 'name']


class SealColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealColor
        fields = ['id', 'name']


class ShprosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpros
        fields = ['id', 'name']


class ShtapikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shtapik
        fields = ['id', 'name']


class SashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sash
        fields = ['id', 'name']


class LaminationOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination_outside
        fields = ['id', 'name']


class LaminationInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination_inside
        fields = ['id', 'name']


class ProfileWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_weight
        fields = ['id', 'name']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name']


class ProductsInstallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_install
        fields = ['id', 'name']


class PvcSlopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pvc_slopes
        fields = ['id', 'name']


class FreePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Free_positions
        fields = ['id', 'name']


class FavoritePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_positions
        fields = ['id', 'name']


class WindowsillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill
        fields = ['id', 'name']


class WindowsillDankeKomfortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill_danke_komfort
        fields = ['id', 'name']


class WindowsillDankeStandartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill_danke_standart
        fields = ['id', 'name']


class WindowsillDankePremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill_danke_premium
        fields = ['id', 'name']


class LowTidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Low_tides
        fields = ['id', 'name']


class VisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visors
        fields = ['id', 'name']


class FlashingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashing
        fields = ['id', 'name']


class FlashingMetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashing_metal
        fields = ['id', 'name']


class PlatbandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platband
        fields = ['id', 'name']


class ExtensionsToProfile60Serializer(serializers.ModelSerializer):
    class Meta:
        model = Extensions_to_profile_sixty
        fields = ['id', 'name']


class ExtensionsToProfile70Serializer(serializers.ModelSerializer):
    class Meta:
        model = Extensions_to_profile_seventy
        fields = ['id', 'name']


class BayWindowToProfile60Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bay_window_to_profile_sixty
        fields = ['id', 'name']


class BayWindowToProfile70Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bay_window_to_profile_seventy
        fields = ['id', 'name']


class Connector90gSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector_90g
        fields = ['id', 'name']


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['id', 'name']


class HandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handles
        fields = ['id', 'name']


class LocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locks
        fields = ['id', 'name']


class StraightConnectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Straight_connectors
        fields = ['id', 'name']


class SupplyValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_valve
        fields = ['id', 'name']


class ConstructorSerializer(serializers.ModelSerializer):
    price = PriceSerializer(allow_null=True)
    product_type = ProductTypeSerializer(allow_null=True)
    profile = ProfileSerializer(allow_null=True)
    aggregate = AggregateSerializer(allow_null=True)
    fittings = FittingsSerializer(allow_null=True)
    seal_outside = SealOutsideSerializer(allow_null=True)
    seal_rebate = SealRebateSerializer(allow_null=True)
    seal_internal = SealInternalSerializer(allow_null=True)
    seal_color = SealColorSerializer(allow_null=True)
    shpros = ShprosSerializer(allow_null=True)
    shtapik = ShtapikSerializer(allow_null=True)
    sash = SashSerializer(allow_null=True)
    lamination_outside = LaminationOutsideSerializer(allow_null=True)
    lamination_inside = LaminationInsideSerializer(allow_null=True)
    profile_weight = ProfileWeightSerializer(allow_null=True)
    note = NoteSerializer(allow_null=True)
    products_install = ProductsInstallSerializer(allow_null=True)
    pvc_slopes = PvcSlopesSerializer(allow_null=True)
    free_positions = FreePositionsSerializer(allow_null=True)
    favorite_positions = FavoritePositionsSerializer(allow_null=True)
    windowsill = WindowsillSerializer(allow_null=True)
    windowsill_danke_komfort = WindowsillDankeKomfortSerializer(allow_null=True)
    windowsill_danke_standart = WindowsillDankeStandartSerializer(allow_null=True)
    windowsill_danke_premium = WindowsillDankePremiumSerializer(allow_null=True)
    low_tides = LowTidesSerializer(allow_null=True)
    visors = VisorsSerializer(allow_null=True)
    flashing = FlashingSerializer(allow_null=True)
    flashing_metal = FlashingMetalSerializer(allow_null=True)
    platband = PlatbandSerializer(allow_null=True)
    extensions_to_profile60 = ExtensionsToProfile60Serializer(allow_null=True)
    extensions_to_profile70 = ExtensionsToProfile70Serializer(allow_null=True)
    bay_window_to_profile60 = BayWindowToProfile60Serializer(allow_null=True)
    bay_window_to_profile70 = BayWindowToProfile70Serializer(allow_null=True)
    connector_90g = Connector90gSerializer(allow_null=True)
    accessories = AccessoriesSerializer(allow_null=True)
    handles = HandlesSerializer(allow_null=True)
    locks = LocksSerializer(allow_null=True)
    straight_connectors = StraightConnectorsSerializer(allow_null=True)
    supply_valve = SupplyValveSerializer(allow_null=True)

    class Meta:
        model = Constructor
        fields = '__all__'
