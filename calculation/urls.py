from django.urls import path, include
from .views import *


urlpatterns = [
    # path('window/', CalculationViewSet.as_view({'get': 'list'})),
    path('window/', CalculationWindowAPIView.as_view()),
    path('windowsill', CalculationWindowsillAPIView.as_view()),
    path('low-tides', CalculationLowTidesAPIView.as_view()),



]
