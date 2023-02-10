
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from .models import *
from rest_framework import generics, viewsets, mixins
from .serializer import *
import requests


class CallsTableGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin

):
    queryset = CallsTable.objects.all().order_by('-id')
    serializer_class = CallsTableSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({'data': self.retrieve(request, pk).data})

        return self.list(request)

