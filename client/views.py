from django.core.paginator import Paginator
from django.http import JsonResponse
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

    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        number_id = create_number_record(request.data['numbers']['number'], request.data['numbers']['name'])
        calls = create_calls_record(request.data['numbers'])
        address_id = create_address_record(request.data['addresses'])

        client = Client.objects.create(
            name=request.data['name'],
            author=user,  # get current user
        )

        client.addresses.add(address_id)
        client.numbers.add(number_id)
        for call in calls:
            client.calls.add(call['id'])

        return Response({'data': serializer.data})


class ClientsRecordsView(generics.ListAPIView):  # get all clients for pagination
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = CustomPagination


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()  # .values().order_by('-id')
    serializer_class = ClientSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch']


class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']
