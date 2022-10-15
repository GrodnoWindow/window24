from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import WindowDiscount
from .utils import *
from constructor.serializer import ConstructorSerializer
from .serializer import ConstructorCalcSerializer, WindowsillCalcSerializer, LowTidesCalcSerializer
from constructor.models import Constructor
from .utils import *
from django.forms import model_to_dict


class CalculationWindowAPIView(APIView):
    serializer_class = ConstructorCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile_id = request.data['window']['profile_id']
        fittings_id = request.data['window']['fittings_id']
        currency = request.data['currency']
        price_input = request.data['price_input']
        price_output = calc_window_disc(profile_id=profile_id, fittings_id=fittings_id, currency=currency,
                                        price=price_input)
        print(price_output)
        # calc_window_disc(profile_id = request.data['profile'][],
        #                  fittings_id=request.data['fittings'],
        #                  currency=['currency'], price=request.data['price'])
        # number_id = create_number_record(request.data['numbers'])
        # calls = create_calls_record(request.data['numbers'])
        # address_id = create_address_record(request.data['addresses'])

        # client = Constructor.objects.create(
        #
        # )
        # name = request.data['name'],
        #
        # client.addresses.add(address_id)
        # client.numbers.add(number_id)
        # for call in calls:
        #     client.calls.add(call['id'])

        return Response({'data': serializer.data})


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
        windowsill_calc = calc_windowsill(windowsill_id=windowsill_id, width=width, length=length, count=count)

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

        low_tides_calc = calc_low_tides(low_tides_id=low_tides_id, width=width, length=length, count=count)

        return Response({'data': model_to_dict(low_tides_calc)})
