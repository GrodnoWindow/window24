import coreschema as coreschema
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.viewsets import GenericViewSet
from .serializer import MiscalculationSerializer
from .models import *

from config.pagination import CustomPagination


class MiscalculationAPIList(generics.ListCreateAPIView): # GET and POST requests
    queryset = Miscalculation.objects.all()
    serializer_class = MiscalculationSerializer
    pagination_class = CustomPagination


class MiscalculationViewSet(mixins.CreateModelMixin, # viewsets.ModelViewSet
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): # get, post , get<id>, put<id>, path<id>

    queryset = Miscalculation.objects.all()
    serializer_class = MiscalculationSerializer
    pagination_class = CustomPagination

    # def get_queryset(self, *args, **kwargs):
    #     if self.request.query_params == {}:
    #         queryset = Miscalculation.objects.all()
    #     else:
    #         overdue = self.request.query_params.get('overdue')
    #         author = self.request.query_params.get('author')
    #         queryset = Miscalculation.objects.filter(overdue=overdue, author=author).order_by('time_create')
    #
    #     return queryset