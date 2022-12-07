from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'constructor', ConstructorViewSet, basename='constructor')


urlpatterns = [

    path('', include(router.urls)),

    # path('constructor/', CalculationConstructorAPIView.as_view()),
    path('window/', CalculationWindowAPIView.as_view()),
    path('windowsill/', CalculationWindowsillAPIView.as_view()),
    path('low-tides/', CalculationLowTidesAPIView.as_view()),
    # path('works/', WorksGenericAPIView.as_view()),



]
