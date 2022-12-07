import coreschema as coreschema
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.viewsets import GenericViewSet
from .serializer import MiscalculationSerializer
from .models import *

from config.pagination import CustomPagination


# class MiscalculationAPIList(generics.ListCreateAPIView):  # GET and POST requests
#     queryset = Miscalculation.objects.all()
#     serializer_class = MiscalculationSerializer
#     pagination_class = CustomPagination


class MiscalculationViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):  # get, post , get<id>, put<id>, path<id>

    queryset = Miscalculation.objects.all()
    serializer_class = MiscalculationSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Miscalculation.objects.all()
        miscalculation = get_object_or_404(queryset, pk=pk)
        serializer = MiscalculationSerializer(miscalculation)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})
