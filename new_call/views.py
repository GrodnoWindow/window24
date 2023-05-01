from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
# Create your views here.
from rest_framework import generics, viewsets, mixins

from .serializers import OutGoingCallSerializer
import requests


class OutgoingCallGenericAPIView(generics.GenericAPIView, mixins.CreateModelMixin):

    queryset = OutgoingCalls.objects.all()
    serializer_class = OutGoingCallSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = request.data['phone'].replace('+375', '80')
        num_phone = request.data['number']
        if num_phone == 1:
            response = requests.post(f'http://admin:reMont2004@192.168.1.229/servlet?key=number={phone}')
        elif num_phone == 12:
            response = requests.post(f'http://admin:reMont2004@192.168.1.223/servlet?key=number={phone}')

        return Response({"data": response})
