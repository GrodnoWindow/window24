import requests
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics, viewsets, mixins
from .utils import *
from .serializer import *
from .utils import *
from django.forms import model_to_dict
from config.pagination import CustomPagination


class CalculationWindowAPIView(APIView):
    serializer_class = WindowCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile_id = request.data['window']['profile_id']
        fittings_id = request.data['window']['fittings_id']
        currency = request.data['window']['currency_name']
        price_input = request.data['window']['price_input']
        window_calc = calc_window_disc(profile_id=profile_id, fittings_id=fittings_id, currency=currency,
                                       price=price_input)

        return Response({'data': model_to_dict(window_calc)})
        # return Response({'data': serializer.data})


class CalculationWindowsillAPIView(APIView):
    serializer_class = WindowsillCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        windowsill_id = request.data['windowsill_id']
        print(windowsill_id)
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']
        windowsill_calc = calc_windowsill(windowsill_id=windowsill_id, width=width,
                                          length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(windowsill_calc)})


class CalculationLowTidesAPIView(APIView):
    serializer_class = LowTidesCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        low_tides_id = request.data['low_tides_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        low_tides_calc = calc_low_tides(low_tides_id=low_tides_id, width=width,
                                        length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(low_tides_calc)})


class CalculationFlashingAPIView(APIView):
    serializer_class = FlashingCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        flashing_id = request.data['flashing_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        flashing_calc = calc_flashing(flashing_id=flashing_id, width=width,
                                      length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(flashing_calc)})


class CalculationCasingAPIView(APIView):
    serializer_class = CasingCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        casing_id = request.data['casing_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        casing_calc = calc_casing(casing_id=casing_id, width=width,
                                  length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(casing_calc)})


class CalculationVisorsAPIView(APIView):
    serializer_class = VisorsCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        visors_id = request.data['visors_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        visors_calc = calc_visors(visors_id=visors_id, width=width,
                                  length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(visors_calc)})


class ConstructorViewSet(viewsets.ModelViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Constructor.objects.all()
        serializer = ConstructorSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Constructor.objects.all()
        mail = get_object_or_404(queryset, pk=pk)
        serializer = ConstructorSerializer(mail)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        constructor = Constructor.objects.create(
            product_type=request.data['product_type'],
            door=request.data['door'],
            aggregate=request.data['aggregate'],
            lamination=request.data['lamination'],
            shtapik=request.data['shtapik'],
            sash=request.data['sash'],
            gorbylki=request.data['gorbylki'],
            handles=request.data['handles'],
            connection_profile=request.data['connection_profile'],
            additional_profile=request.data['additional_profile'],
            sealant=request.data['sealant'],
            other_complectation=request.data['other_complectation'],
            price_constructor=request.data['price_constructor'],

            )
        try:
            for i in request.data['windowsills_calc']:
                constructor.windowsills_calc.add(i)
        except:
            pass
        try:
            for i in request.data['casing_calc']:
                constructor.casing_calc.add(i)
        except:
            pass
        try:
            for i in request.data['flashing_calc']:
                constructor.flashing_calc.add(i)
        except:
            pass
        try:
            for i in request.data['visors_calc']:
                constructor.visors_calc.add(i)
        except:
            pass
        try:
            for i in request.data['lowtides_calc']:
                constructor.lowtides_calc.add(i)
        except:
            pass
        try:
            for i in request.data['works']:
                constructor.works.add(i)
        except:
            pass

        return Response({'data': request.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        constructor = Constructor.objects.get(id=instance.pk)

        constructor.is_active = request.data['is_active']
        constructor.price_window = request.data["price_window"]
        constructor.price_material = request.data["price_material"]
        constructor.price_constructor = request.data["price_constructor"]
        constructor.product_type = request.data["product_type"]
        constructor.aggregate = request.data["aggregate"]
        constructor.seal_outside = request.data["seal_outside"]
        constructor.seal_rebate = request.data["seal_rebate"]
        constructor.seal_internal = request.data["seal_internal"]
        constructor.seal_color = request.data["seal_color"]
        constructor.shpros = request.data["shpros"]
        constructor.shtapik = request.data["shtapik"]
        constructor.sash = request.data["sash"]
        constructor.lamination_outside = request.data["lamination_outside"]
        constructor.lamination_inside = request.data["lamination_inside"]
        constructor.profile_weight = request.data["profile_weight"]
        constructor.note = request.data["note"]
        constructor.products_install = request.data["products_install"]
        constructor.pvc_slopes = request.data["pvc_slopes"]
        constructor.free_positions = request.data["free_positions"]
        constructor.favorite_positions = request.data["favorite_positions"]
        # windowsill=request.data["windowsill"],
        constructor.visors = request.data["visors"]
        constructor.flashing = request.data["flashing"]
        constructor.flashing_metal = request.data["flashing_metal"]
        constructor.platband = request.data["platband"]
        constructor.extensions_to_profile60 = request.data["extensions_to_profile60"]
        constructor.extensions_to_profile70 = request.data["extensions_to_profile70"]
        constructor.bay_window_to_profile60 = request.data["bay_window_to_profile60"]
        constructor.bay_window_to_profile70 = request.data["bay_window_to_profile70"]
        constructor.connector_90g = request.data["connector_90g"]
        constructor.accessories = request.data["accessories"]
        constructor.handles = request.data["handles"]
        constructor.locks = request.data["locks"]
        constructor.straight_connectors = request.data["straight_connectors"]
        constructor.supply_valve = request.data["supply_valve"]
        constructor.window_calc = request.data["window_calc"]

        constructor.windowsills_calc.clear()
        constructor.lowtides_calc.clear()
        constructor.works.clear()

        try:
            for i in request.data['windowsills_calc']:
                constructor.windowsills_calc.add(i)
        except:
            pass
        try:
            for i in request.data['lowtides_calc']:
                constructor.lowtides_calc.add(i)
        except:
            pass
        try:
            for i in request.data['works']:
                constructor.works.add(i)
        except:
            pass

        serializer = ConstructorSerializer(constructor)
        return Response({"data": serializer.data})


class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Door.objects.all()
        serializer = DoorSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Door.objects.all()
        door = get_object_or_404(queryset, pk=pk)
        serializer = DoorSerializer(door)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class LaminationViewSet(viewsets.ModelViewSet):
    queryset = Lamination.objects.all()
    serializer_class = LaminationSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Lamination.objects.all()
        serializer = LaminationSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Door.objects.all()
        lamination = get_object_or_404(queryset, pk=pk)
        serializer = LaminationSerializer(lamination)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class ConnectionProfileViewSet(viewsets.ModelViewSet):
    queryset = ConnectionProfile.objects.all()
    serializer_class = ConnectionProfileSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = ConnectionProfile.objects.all()
        serializer = ConnectionProfileSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = ConnectionProfile.objects.all()
        connection_profile = get_object_or_404(queryset, pk=pk)
        serializer = ConnectionProfileSerializer(connection_profile)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class AdditionalProfileViewSet(viewsets.ModelViewSet):
    queryset = AdditionalProfile.objects.all()
    serializer_class = AdditionalProfileSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = AdditionalProfile.objects.all()
        serializer = AdditionalProfileSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = AdditionalProfile.objects.all()
        additional_profile = get_object_or_404(queryset, pk=pk)
        serializer = AdditionalProfileSerializer(additional_profile)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class SealantViewSet(viewsets.ModelViewSet):
    queryset = Sealant.objects.all()
    serializer_class = SealantSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Sealant.objects.all()
        serializer = SealantSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Sealant.objects.all()
        sealant = get_object_or_404(queryset, pk=pk)
        serializer = SealantSerializer(sealant)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})
