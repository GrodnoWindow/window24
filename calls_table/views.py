
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from .models import *
from rest_framework import generics, viewsets, mixins
from .serializer import *
import requests


class CallsTableGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    queryset = CallsTable.objects.all().order_by('-id')
    serializer_class = CallsTableSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({'data': self.retrieve(request, pk).data})

        return self.list(request)


class CallsTableAPIView(generics.ListAPIView):  # all requests get,put,patch ...
    queryset = CallsTable.objects.all()
    serializer_class = CallsTableSerializer

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        w = CallsTable.objects.get(pk=pk)
        return Response({"data": CallsTableSerializer(w).data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = CallsTable.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = CallsTableSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})


class OutgoingCallViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                          GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = OutgoingCalls.objects.all()
    serializer_class = OutGoingCallSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = request.data['phone'].replace('+375', '80')
        num_phone = request.data['number']
        if num_phone == 1:
            response = requests.post(f'http://admin:hjvxbr228@192.168.1.229/servlet?key=number={phone}')
        elif num_phone == 2:
            response = requests.post(f'http://admin:hjvxbr228@192.168.1.223/servlet?key=number={phone}')
            print(response)
        return Response({"data": response})
