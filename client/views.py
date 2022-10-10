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

        numbers = create_number_record(request.data['numbers'])
        if not numbers:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        calls = create_calls_record(request.data['numbers'])
        addresses = create_address_record(request.data['addresses'])

        client = Client.objects.create(
            name=request.data['name'],
            author=user,  # get current user
        )

        for address in addresses:
            client.addresses.add(address['id'])

        for call in calls:
            client.calls.add(call['id'])

        for num in numbers:
            client.numbers.add(num['id'])

        # calls = add_calls_to_client(request.data['number'])
        # client.calls.add(1)

        return Response({'data': serializer.data})


class ClientViewSet(  # mixins.CreateModelMixin, # POST REQUESTS
    mixins.RetrieveModelMixin,  # get all, get<id>,
    mixins.UpdateModelMixin,  # put<id>, patch<id>
    GenericViewSet):
    queryset = Client.objects.all()  # .values().order_by('-id')
    serializer_class = ClientSerializer


class ClientsRecordsView(generics.ListAPIView):  # get all clients for pagination
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = CustomPagination



