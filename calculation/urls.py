from django.urls import path, include
from .views import *


urlpatterns = [
    # path('window/', CalculationViewSet.as_view({'get': 'list'})),
    path('window/', CalculationAPIView.as_view()),


]