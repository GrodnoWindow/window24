from datetime import datetime

import coreschema as coreschema
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.viewsets import GenericViewSet
from .serializer import MiscalculationSerializer
from .models import *

from config.pagination import CustomPagination




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
        miscalculation = Miscalculation.objects.create(created_time=datetime.now(),last_update_time=datetime.now())
        miscalculation.author = request.user.username

        try:
            for constructors in request.data['constructors']:
                miscalculation.constructors.add(constructors)
            for constructors in miscalculation.constructors.all():
                miscalculation.sum += constructors.price_constructor
        except:
            pass
        try:
            miscalculation.status = request.data['status']
        except:
            pass
        try:
            miscalculation.offer = request.data['offer']
        except:
            pass

        miscalculation.save()
        serializer = MiscalculationSerializer(miscalculation)

        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Miscalculation.objects.all()
        miscalculation = get_object_or_404(queryset, pk=pk)
        serializer = MiscalculationSerializer(miscalculation)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        miscalculation_id = instance.id
        miscalculation = Miscalculation.objects.get(pk=miscalculation_id)
        miscalculation.sum = 0
        try:
            miscalculation.constructors.clear()  # Очистка связанных конструкторов

            for constructor_id in request.data.get('constructors', []):
                constructor = Constructor.objects.get(pk=constructor_id)
                miscalculation.constructors.add(constructor)

            # Подсчет суммы
            sum_price = sum(constructor.price_constructor for constructor in miscalculation.constructors.all())
            miscalculation.sum = sum_price

            # Обновление остальных полей
            miscalculation.status = request.data['status']
            miscalculation.author = request.user.username

            miscalculation.save()

            serializer = MiscalculationSerializer(miscalculation)
            return Response({"data": serializer.data})
        except Miscalculation.DoesNotExist:
            return Response({'error': 'Miscalculation not found.'}, status=status.HTTP_404_NOT_FOUND)

