from .models import Constructor
from .serializer import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, mixins
from rest_framework.response import Response
from config.pagination import CustomPagination
from rest_framework import views
from call.models import Call
from client.models import Client
from .models import *


class ConstructorGenericAPIList(generics.ListAPIView):  # get all fields constructor
    queryset = Constructor.objects.all()
    serializer_class = ConstructorFieldsSerializer
    pagination_class = CustomPagination
    # def get(self, request, pk=None):
    #     if pk:
    #         return Response({
    #             'calls': self.retrieve(request, pk).data
    #         })
    #
    #     return self.list(request)



class ConstructorCreateApi(generics.CreateAPIView):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer


class ConstructorViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         GenericViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
