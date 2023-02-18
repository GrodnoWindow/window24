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


class SealantColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantColor
        fields = ['id', 'name']


class SealantInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantInside
        fields = ['id', 'name']


class SealantOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantOutside
        fields = ['id', 'name']


class SealantShtapikSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantShtapik
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


class WindowsillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Windowsill
        fields = '__all__'


class LowTidesSerializer(serializers.ModelSerializer):

    class Meta:
        model = LowTides
        fields = '__all__'

class VisorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visors
        fields = '__all__'


class FlashingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashing
        fields = '__all__'


class HandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherComplectation
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


class CasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casing
        fields = '__all__'


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'name', 'price']


class GorbylkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gorbylki
        fields = '__all__'


class OtherComplectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherComplectation
        fields = '__all__'


class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening
        fields = '__all__'


class LockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lock
        fields = '__all__'


class DoorHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorHandles
        fields = '__all__'


class DoorHingesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorHinges
        fields = '__all__'


class CylinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cylinder
        fields = '__all__'


class DoorCloserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorCloser
        fields = '__all__'


class OpeningLimiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningLimiter
        fields = '__all__'


class TypeLaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLamination
        fields = '__all__'


class TypeLamination1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLamination2
        fields = '__all__'


class SealBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealBasic
        fields = '__all__'


class ArticleAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAdditionalProfile
        fields = '__all__'


class ConnectionProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionProfileName
        fields = '__all__'


class ColorInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorInside
        fields = '__all__'


class ColorOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorOutside
        fields = '__all__'


class ConstructorSerializer(serializers.Serializer):
    profile = ProfileSerializer(read_only=True, many=True)
    product_type = ProductTypeSerializer(read_only=True, many=True)
    aggregate = AggregateSerializer(read_only=True, many=True)
    fittings = FittingsSerializer(read_only=True, many=True)
    seal_outside = SealOutsideSerializer(read_only=True, many=True)
    seal_rebate = SealRebateSerializer(read_only=True, many=True)
    seal_internal = SealInternalSerializer(read_only=True, many=True)
    shpros = ShprosSerializer(read_only=True, many=True)
    shtapik = ShtapikSerializer(read_only=True, many=True)
    sash = SashSerializer(read_only=True, many=True)
    lamination_outside = LaminationOutsideSerializer(read_only=True, many=True)
    lamination_inside = LaminationInsideSerializer(read_only=True, many=True)
    profile_weight = ProfileWeightSerializer(read_only=True, many=True)
    note = NoteSerializer(read_only=True, many=True)
    products_install = ProductsInstallSerializer(read_only=True, many=True)
    pvc_slopes = PvcSlopesSerializer(read_only=True, many=True)
    windowsill = WindowsillSerializer(read_only=True, many=True)
    low_tides = LowTidesSerializer(read_only=True, many=True)
    visors = VisorsSerializer(read_only=True, many=True)
    flashing = FlashingSerializer(read_only=True, many=True)
    handles = HandlesSerializer(read_only=True, many=True)
    locks = LocksSerializer(read_only=True, many=True)
    straight_connectors = StraightConnectorsSerializer(read_only=True, many=True)
    supply_valve = CasingSerializer(read_only=True, many=True)
    works = WorksSerializer(read_only=True, many=True)
    other_complectation = OtherComplectationSerializer(read_only=True, many=True)
    gorbylki = GorbylkiSerializer(read_only=True, many=True)
    opening = OpeningSerializer(read_only=True, many=True)
    lock = LockSerializer(read_only=True, many=True)
    handle = DoorHandleSerializer(read_only=True, many=True)
    door_hinges = DoorHingesSerializer(read_only=True, many=True)
    cylinder = CylinderSerializer(read_only=True, many=True)
    door_closer = DoorCloserSerializer(read_only=True, many=True)
    opening_limiter = OpeningLimiterSerializer(read_only=True, many=True)
    type_lamination = TypeLaminationSerializer(read_only=True, many=True)
    type_lamination1 = TypeLamination1Serializer(read_only=True, many=True)
    seal_basic = SealBasicSerializer(read_only=True, many=True)
    article = ArticleAdditionalSerializer(read_only=True, many=True)
    connection_profile_name = ConnectionProfileNameSerializer(read_only=True, many=True)
    color_inside = ColorInsideSerializer(read_only=True, many=True)
    color_outside = ColorOutsideSerializer(read_only=True, many=True)
    sealant_color = SealantColorSerializer(read_only=True, many=True)
    sealant_inside = SealantInsideSerializer(read_only=True, many=True)
    sealant_outside = SealantOutsideSerializer(read_only=True, many=True)
    sealant_shtapik = SealantShtapikSerializer(read_only=True, many=True)
    casing = CasingSerializer(read_only=True, many=True)
