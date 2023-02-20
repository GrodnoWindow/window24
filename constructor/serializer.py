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


class WindowsillColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillColor
        fields = '__all__'


class WindowsillInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillInstallation
        fields = '__all__'


class WindowsillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill
        fields = '__all__'


class LowTidesColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesColor
        fields = '__all__'


class LowTidesInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesInstallation
        fields = '__all__'


class LowTidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTides
        fields = '__all__'


class VisorsColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisorsColor
        fields = '__all__'


class VisorsInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisorsInstallation
        fields = '__all__'


class VisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visors
        fields = '__all__'


class SlopesOfMetalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetalColor
        fields = '__all__'


class SlopesOfMetalInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetalInstallation
        fields = '__all__'


class SlopesOfMetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetal
        fields = '__all__'


class MountingMaterialsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterialsName
        fields = '__all__'


class MountingMaterialsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterialsType
        fields = '__all__'


class FlashingColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashingColor
        fields = '__all__'


class FlashingInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashingInstallation
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


class CasingColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingColor
        fields = '__all__'


class CasingFasteningSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingFastening
        fields = '__all__'


class CasingInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingInstallation
        fields = '__all__'


class CasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casing
        fields = '__all__'


class InternalSlopeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlope
        fields = '__all__'


class InternalSlopeInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlopeInstallation
        fields = '__all__'


class InternalSlopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlope
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
    windowsill_color = WindowsillColorSerializer(read_only=True, many=True)
    windowsill_installation = WindowsillInstallationSerializer(read_only=True, many=True)
    windowsill = WindowsillSerializer(read_only=True, many=True)
    casing_fastening = CasingFasteningSerializer(read_only=True, many=True)
    casing_color = CasingColorSerializer(read_only=True, many=True)
    casing_installation = CasingInstallationSerializer(read_only=True, many=True)
    casing = CasingSerializer(read_only=True, many=True)
    flashing_color = FlashingColorSerializer(read_only=True, many=True)
    flashing_installation = FlashingInstallationSerializer(read_only=True, many=True)
    flashing = FlashingSerializer(read_only=True, many=True)
    internal_slope_color = InternalSlopeColorSerializer(read_only=True, many=True)
    internal_slope_installation = InternalSlopeInstallationSerializer(read_only=True, many=True)
    internal_slope = InternalSlopeSerializer(read_only=True, many=True)
    low_tides_color = LowTidesColorSerializer(read_only=True, many=True)
    low_tides_installation = LowTidesInstallationSerializer(read_only=True, many=True)
    low_tides = LowTidesSerializer(read_only=True, many=True)
    visors_color = VisorsColorSerializer(read_only=True, many=True)
    visors_installation = VisorsInstallationSerializer(read_only=True, many=True)
    visors = VisorsSerializer(read_only=True, many=True)
    slopes_of_metal_color = SlopesOfMetalColorSerializer(read_only=True, many=True)
    slopes_of_metal_installation = SlopesOfMetalInstallationSerializer(read_only=True, many=True)
    slopes_of_metal = SlopesOfMetalSerializer(read_only=True, many=True)
    mounting_materials_type = MountingMaterialsTypeSerializer(read_only=True, many=True)
    mounting_materials_name = MountingMaterialsNameSerializer(read_only=True, many=True)
