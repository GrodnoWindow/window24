from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter




urlpatterns = [
    # path('window/', ConstructorWindowAPIView.as_view()),
    # path('extrawork/', ConstructorExtraWorkAPIView.as_view()),
    # path('extramaterial/', ConstructorExtraMaterialAPIView.as_view()),

    # path('category/equipment/', ConstructorEquipmentAPIView.as_view()),
    # path('category/low-tides/', ConstructorLowTidesAPIView.as_view()),
    # path('category/lamination/', ConstructorLaminationsAPIView.as_view()),
    # path('category/additional-option/', ConstructorAdditionOptionAPIView.as_view()),
    # path('category/material/', ConstructorMaterialAPIView.as_view()),
    # path('category/works/', WorksAPIView.as_view()),

    path('category/equipment/', EquipmentAPIView.as_view()),
    path('category/equipment/lamination/', LaminationAPIView.as_view()),
    path('category/equipment/door/', DoorAPIView.as_view()),
    path('category/equipment/connection-profile/', ConnectionProfileAPIView.as_view()),
    path('category/equipment/additional-profile/', AdditionalProfileAPIView.as_view()),
    path('category/equipment/sealant/', SealantAPIView.as_view()),

]
