from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter


router_constructor = SimpleRouter()
router_constructor.register(r'constructor', ConstructorViewSet, basename='constructor')

router_door = SimpleRouter()
router_door.register(r'door', DoorViewSet, basename='door')


router_lamination = SimpleRouter()
router_lamination.register(r'lamination', LaminationViewSet, basename='lamination')

router_connection_profile = SimpleRouter()
router_connection_profile.register(r'connection-profile', ConnectionProfileViewSet, basename='connection profile')

router_additional_profile = SimpleRouter()
router_additional_profile.register(r'connection-profile', AdditionalProfileViewSet, basename='additional profile')

router_sealant = SimpleRouter()
router_sealant.register(r'sealant', SealantViewSet, basename='sealant')


urlpatterns = [

    path('', include(router_constructor.urls)),

    # path('constructor/', CalculationConstructorAPIView.as_view()),
    path('calculation/window/', CalculationWindowAPIView.as_view()),
    path('calculation/windowsill/', CalculationWindowsillAPIView.as_view()),
    path('calculation/low-tides/', CalculationLowTidesAPIView.as_view()),
    path('equipment/', include(router_door.urls)),
    path('equipment/', include(router_lamination.urls)),
    path('equipment/', include(router_connection_profile.urls)),
    path('equipment/', include(router_additional_profile.urls)),
    path('equipment/', include(router_sealant.urls)),

    # path('works/', WorksGenericAPIView.as_view()),



]
