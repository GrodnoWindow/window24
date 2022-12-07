import coreschema as coreschema
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.viewsets import GenericViewSet
from .serializer import ComplaintSerializer
from .models import *

from config.pagination import CustomPagination


class ComplaintAPIList(generics.ListCreateAPIView): # GET and POST requests
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    pagination_class = CustomPagination


class ComplaintViewSet(mixins.CreateModelMixin, # viewsets.ModelViewSet
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): # get, post , get<id>, put<id>, path<id>

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    pagination_class = CustomPagination
