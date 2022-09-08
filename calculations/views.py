from calculations.seializer import CalculationsSerializer
from calculations.models import Calculations
from rest_framework import generics, viewsets


class CaclulationViewSet(viewsets.ModelViewSet):
    queryset = Calculations.objects.all()
    serializer_class = CalculationsSerializer

    def get_queryset(self):
        queryset = Calculations.objects.all()
        return queryset