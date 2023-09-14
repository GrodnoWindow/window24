from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Contract
from .serializer_old import *
from rest_framework import viewsets, mixins, status, generics
from rest_framework.response import Response
from .utils import *
from config.pagination import CustomPagination

from call.models import CallWindow

# @permission_classes([IsAuthenticated])
# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all().order_by('-id')
#     serializer_class = OrderSerializer
#     http_method_names = ['get', 'patch', 'post']
#     pagination_class = CustomPagination


# @permission_classes([IsAuthenticated])
class ClientViewSet(viewsets.ModelViewSet):  # get, post , get<id>, put<id>, path<id>
    queryset = Client.objects.all().order_by('-id')
    serializer_class = ClientSerializer
    http_method_names = ['get', 'patch', 'post']
    pagination_class = CustomPagination


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {"data": serializer.data}
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {"data": serializer.data}
        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {"data": serializer.data}
        return Response(data, status=201, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = {"data": serializer.data}
        return Response(data)


class NumberViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Number.objects.all()
        number = get_object_or_404(queryset, pk=pk)
        serializer = NumberSerializer(number)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})


class AddressViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(address)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})


class PrompterViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Prompter.objects.all()
    serializer_class = PrompterSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Prompter.objects.all()
        prompter = get_object_or_404(queryset, pk=pk)
        serializer = PrompterSerializer(prompter)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})


class ContractViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        last_contract = Contract.objects.order_by('-id').first()
        last_number = int(last_contract.number) if last_contract else 0
        new_number = last_number + 1

        passport_details = PassportDetails.objects.get(pk=request.data['passport_details'])


        contract = Contract.objects.create(
            date=request.data['date'],
            delivery_address=request.data['delivery_address'],
            phone=request.data['phone'],
            cost=request.data['cost'],
            deposit=request.data['deposit'],
            finish_cost=request.data['finish_cost'],
            signed=request.data['signed'],
            number=new_number,
            passport_details=passport_details,
        )

        contract.save()
        serializer_contract = ContractSerializer(contract)
        return Response({"data": serializer_contract.data})

    def retrieve(self, request, pk=None):
        queryset = Contract.objects.all()
        contract = get_object_or_404(queryset, pk=pk)
        serializer = NumberSerializer(contract)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})


class PassportDetailsViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = PassportDetails.objects.all()
    serializer_class = PassportDetailsSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = PassportDetails.objects.all()
        passport = get_object_or_404(queryset, pk=pk)
        serializer = NumberSerializer(passport)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})
