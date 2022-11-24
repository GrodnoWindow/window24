from rest_framework import serializers
from .models import *
from calculation.models import Constructor


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name']


class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = ['id', 'name']


class FittingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fittings
        fields = ['id', 'name']


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
        model = LaminationOutside
        fields = ['id', 'name']


class LaminationInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaminationInside
        fields = ['id', 'name']


class ProfileWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileWeight
        fields = ['id', 'name']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name']


class ProductsInstallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInstall
        fields = ['id', 'name']


class PvcSlopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PvcSlopes
        fields = ['id', 'name']


class FreePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreePositions
        fields = ['id', 'name']


class FavoritePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePositions
        fields = ['id', 'name']


class WindowsillColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillColor
        fields = ['id', 'name']


class WindowsillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillType
        fields = ['id', 'name']


class WindowsillSerializer(serializers.ModelSerializer):
    color = WindowsillColorSerializer(many=False, read_only=False)
    type = WindowsillTypeSerializer(many=False, read_only=False)

    class Meta:
        model = Windowsill
        fields = ['id', 'color', 'type']


# class WindowsillDankeKomfortSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WindowsillDankeKomfort
#         fields = ['id', 'name']
#
#
# class WindowsillDankeStandartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WindowsillDankeStandart
#         fields = ['id', 'name']
#
#
# class WindowsillDankePremiumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WindowsillDankePremium
#         fields = ['id', 'name']
class LowTidesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesType
        fields = '__all__'


class LowTidesSerializer(serializers.ModelSerializer):
    type = LowTidesTypeSerializer(many=False, read_only=False)

    class Meta:
        model = LowTides
        fields = ['id', 'name', 'type']


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
        model = FlashingMetal
        fields = ['id', 'name']


class PlatbandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platband
        fields = ['id', 'name']


class ExtensionsToProfile60Serializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionsToProfile70
        fields = ['id', 'name']


class ExtensionsToProfile70Serializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionsToProfile70
        fields = ['id', 'name']


class BayWindowToProfile60Serializer(serializers.ModelSerializer):
    class Meta:
        model = BayWindowToProfile60
        fields = ['id', 'name']


class BayWindowToProfile70Serializer(serializers.ModelSerializer):
    class Meta:
        model = BayWindowToProfile70
        fields = ['id', 'name']


class Connector90gSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector90g
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
        model = StraightConnectors
        fields = ['id', 'name']


class SupplyValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyValve
        fields = ['id', 'name']


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'name', 'price']


class ConstructorSerializer(serializers.Serializer):
    profile = ProfileSerializer(read_only=True, many=True)
    product_type = ProductTypeSerializer(read_only=True, many=True)
    aggregate = AggregateSerializer(read_only=True, many=True)
    fittings = FittingsSerializer(read_only=True, many=True)
    seal_outside = SealOutsideSerializer(read_only=True, many=True)
    seal_rebate = SealRebateSerializer(read_only=True, many=True)
    seal_internal = SealInternalSerializer(read_only=True, many=True)
    seal_color = SealColorSerializer(read_only=True, many=True)
    shpros = ShprosSerializer(read_only=True, many=True)
    shtapik = ShtapikSerializer(read_only=True, many=True)
    sash = SashSerializer(read_only=True, many=True)
    lamination_outside = LaminationOutsideSerializer(read_only=True, many=True)
    lamination_inside = LaminationInsideSerializer(read_only=True, many=True)
    profile_weight = ProfileWeightSerializer(read_only=True, many=True)
    note = NoteSerializer(read_only=True, many=True)
    products_install = ProductsInstallSerializer(read_only=True, many=True)
    pvc_slopes = PvcSlopesSerializer(read_only=True, many=True)
    free_positions = FreePositionsSerializer(read_only=True, many=True)
    favorite_positions = FavoritePositionsSerializer(read_only=True, many=True)
    # windowsill = WindowsillSerializer(read_only=True, many=True)
    low_tides = LowTidesSerializer(read_only=True, many=True)
    visors = VisorsSerializer(read_only=True, many=True)
    flashing = FlashingSerializer(read_only=True, many=True)
    flashing_metal = FlashingMetalSerializer(read_only=True, many=True)
    platband = PlatbandSerializer(read_only=True, many=True)
    extensions_to_profile60 = ExtensionsToProfile60Serializer(read_only=True, many=True)
    extensions_to_profile70 = ExtensionsToProfile70Serializer(read_only=True, many=True)
    bay_window_to_profile60 = BayWindowToProfile60Serializer(read_only=True, many=True)
    bay_window_to_profile70 = BayWindowToProfile70Serializer(read_only=True, many=True)
    connector_90g = Connector90gSerializer(read_only=True, many=True)
    accessories = AccessoriesSerializer(read_only=True, many=True)
    handles = HandlesSerializer(read_only=True, many=True)
    locks = LocksSerializer(read_only=True, many=True)
    straight_connectors = StraightConnectorsSerializer(read_only=True, many=True)
    supply_valve = SupplyValveSerializer(read_only=True, many=True)
    works = WorksSerializer(read_only=True, many=True)
