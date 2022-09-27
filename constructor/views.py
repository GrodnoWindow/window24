from .models import Constructor
from .serializer import ConstructorSerializer
from rest_framework import generics, mixins
from rest_framework.viewsets import GenericViewSet


class ConstructorAPIList(generics.ListCreateAPIView):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer


class ConstructorViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
