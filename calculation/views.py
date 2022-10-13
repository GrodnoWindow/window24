from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import WindowDiscount
from .utils import *
from constructor.serializer import ConstructorSerializer
from .serializer import ConstructorCalcSerializer
from constructor.models import Constructor
from .utils import *


class CalculationAPIView(APIView):
    serializer_class = ConstructorCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        print(f"ez nahui 1 : ==={request.data['window']['profile_id']}")
        print(f"ez nahui 1 : ==={request.data['window']['profile_id']}")
        profile_id = request.data['window']['profile_id']
        fittings_id = request.data['window']['fittings_id']
        currency = request.data['currency']
        price_input = request.data['price_input']
        price_output = calc_window_disc(profile_id=profile_id, fittings_id=fittings_id, currency=currency, price=price_input)
        windowsill_id = request.data['windowsills']['windowsill']['id']
        width = request.data['windowsills']['width']
        length = request.data['windowsills']['width']
        count = request.data['windowsills']['width']
        price_output = calc_windowsill(windowsill_id=windowsill_id, width=width, length=length, count=count)
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

# class CalculationViewSet(viewsets.ModelViewSet):
#     serializer_class = WindowsDiscountSerializer
#
#     def get_queryset(self):
#         profile_id = self.request.query_params.get('profile')
#         fittings_id = self.request.query_params.get('fittings')
#         currency = self.request.query_params.get('currency')
#         price = self.request.query_params.get('price')
#
#         sum = calc_window_disc(profile_id=profile_id, fittings_id=fittings_id,
#                                currency=currency, price=price)
