from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .serializer import *
from rest_framework import viewsets, mixins, status, generics
from rest_framework.response import Response
from .utils import *
from config.pagination import CustomPagination

from call.models import Call


class ClientAPIView(APIView):
    serializer_class = ClientPostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        client = Client.objects.create(
            name=request.data['name'],
            category_select=request.data['category_select'],
            author=user.username,  # get current user
        )
        try:
            for number in request.data['numbers']:
                client.numbers.add(number)
                calls = create_calls_record(number)
                for call in calls:
                    client.calls.add(call)
        except:
            pass

        try:
            for address in request.data['addresses']:
                client.addresses.add(address)
        except:
            pass

        try:
            for miscalculation in request.data['miscalculation']:
                client.miscalculation.add(miscalculation)
        except:
            pass
        try:
            for complaint in request.data['complaints']:
                client.complaints.add(complaint)
        except:
            pass
        client.save()

        serializer = ClientSerializer(client)
        return Response({"data": serializer.data})


class ClientPatchAPIView(APIView):
    serializer_class = ClientPostSerializer

    def patch(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        client = Client.objects.get(id=pk)
        client.name = request.data['name']
        client.category_select = request.data['category_select']
        client.author = user.username
        client.numbers.clear()
        client.addresses.clear()
        client.calls.clear()
        client.miscalculation.clear()
        client.complaints.clear()
        try:
            for number in request.data['numbers']:
                client.numbers.add(number)
                calls = create_calls_record(number)
                for call in calls:
                    client.calls.add(call)
        except:
            pass

        try:
            for address in request.data['addresses']:
                client.addresses.add(address)
        except:
            pass

        try:
            for miscalculation in request.data['miscalculation']:
                client.miscalculation.add(miscalculation)
        except:
            pass

        try:
            for complaint in request.data['complaints']:
                client.complaints.add(complaint)
        except:
            pass
        client.save()

        serializer = ClientSerializer(client)
        return Response({"data": serializer.data})


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch']

    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Client.objects.all()
        client = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(client)
        return Response({"data": serializer.data})


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(address)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        address = Address.objects.create(
            name=request.data['name']
        )

        address.save()
        serializer = AddressSerializer(address)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        address = Address.objects.get(pk=pk)
        address.name = request.data['name']
        address.save()
        serializer = AddressSerializer(address)
        return Response({"data": serializer.data})


class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Number.objects.all()
        serializer = NumberSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Number.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = NumberSerializer(address)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        number = Number.objects.create(
            name=request.data['name'],
            number=request.data['number']

        )

        number.save()
        serializer = NumberSerializer(number)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        number = Number.objects.get(pk=pk)
        number.name = request.data['name']
        number.number = request.data['number']
        number.save()
        serializer = NumberSerializer(number)
        return Response({"data": serializer.data})
