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
    path('category/materials/', MaterialsAPIView.as_view()),
    path('category/works/', WorksAPIView.as_view()),

]
