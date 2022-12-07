from rest_framework import viewsets
from .models import *
from .serializer import *
from config.pagination import CustomPagination


class IncomingMailViewSet(viewsets.ModelViewSet):
    queryset = IncomingMail.objects.all()
    serializer_class = IncomingMailSerializer
    # pagination_class = CustomPagination


class OutgoingMailViewSet(viewsets.ModelViewSet):
    queryset = OutgoingMail.objects.all()
    serializer_class = OutgoingMailSerializer
    # pagination_class = CustomPagination
