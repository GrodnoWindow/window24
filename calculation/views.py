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
            is_active=request.data['is_active'],
            price_window=request.data["price_window"],
            price_material=request.data["price_material"],
            price_constructor=request.data["price_constructor"],
            product_type=request.data["product_type"],
            aggregate=request.data["aggregate"],
            seal_outside=request.data["seal_outside"],
            seal_rebate=request.data["seal_rebate"],
            seal_internal=request.data["seal_internal"],
            seal_color=request.data["seal_color"],
            shpros=request.data["shpros"],
            shtapik=request.data["shtapik"],
            sash=request.data["sash"],
            lamination_outside=request.data["lamination_outside"],
            lamination_inside=request.data["lamination_inside"],
            profile_weight=request.data["profile_weight"],
            note=request.data["note"],
            products_install=request.data["products_install"],
            pvc_slopes=request.data["pvc_slopes"],
            free_positions=request.data["free_positions"],
            favorite_positions=request.data["favorite_positions"],
            # windowsill=request.data["windowsill"],
            visors=request.data["visors"],
            flashing=request.data["flashing"],
            flashing_metal=request.data["flashing_metal"],
            platband=request.data["platband"],
            extensions_to_profile60=request.data["extensions_to_profile60"],
            extensions_to_profile70=request.data["extensions_to_profile70"],
            bay_window_to_profile60=request.data["bay_window_to_profile60"],
            bay_window_to_profile70=request.data["bay_window_to_profile70"],
            connector_90g=request.data["connector_90g"],
            accessories=request.data["accessories"],
            handles=request.data["handles"],
            locks=request.data["locks"],
            straight_connectors=request.data["straight_connectors"],
            supply_valve=request.data["supply_valve"],
            window_calc=request.data["window_calc"], )
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
