from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [

    path('category/equipment/main/', EquipmentMainAPIView.as_view()),
    path('category/equipment/extra/', EquipmentExtraAPIView.as_view()),
    path('category/equipment/lamination/', LaminationAPIView.as_view()),
    path('category/equipment/door/', DoorAPIView.as_view()),
    path('category/equipment/connection-profile/', ConnectionProfileAPIView.as_view()),
    path('category/equipment/additional-profile/', AdditionalProfileAPIView.as_view()),
    path('category/equipment/sealant/', SealantAPIView.as_view()),
    path('category/materials/windowsill/', WindowsillAPIView.as_view()),
    path('category/materials/casing/', CasingAPIView.as_view()),
    path('category/materials/flashing/', FlashingAPIView.as_view()),
    path('category/materials/internal-slope/', InternalSlopeAPIView.as_view()),
    path('category/materials/low-tides/', LowTidesAPIView.as_view()),
    path('category/materials/slopes-of-metal/', SlopesOfMetalAPIView.as_view()),
    path('category/materials/visors/', VisorsAPIView.as_view()),
    path('category/materials/mounting-materials/', MountingMaterialsAPIView.as_view()),
    path('category/works/', WorksAPIView.as_view()),
    path('category/provider-window/', ProviderWindowAPIView.as_view()),

]
