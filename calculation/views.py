from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import WindowDiscount
from .serializer import WindowsDiscountSerializer
from .utils import calc_window


# Create your views here.

class CalculationViewSet(viewsets.ModelViewSet):
    serializer_class = WindowsDiscountSerializer

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        fittings_id = self.request.query_params.get('fittings')
        currency = self.request.query_params.get('currency')
        price = self.request.query_params.get('price')

        sum = calc_window(profile_id=profile_id, fittings_id=fittings_id,
                          currency=currency, price=price)


