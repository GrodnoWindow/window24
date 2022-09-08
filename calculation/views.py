from calculations.seializer import CalculationsSerializer
from calculations.models import Calculations
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet


class CaclulationViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Calculations.objects.all()
    serializer_class = CalculationsSerializer

    def get_queryset(self):
        queryset = Calculations.objects.all()
        return queryset