from django.urls import path, include
from .views import *

urlpatterns = [
    # path('window/', ConstructorWindowAPIView.as_view()),
    # path('extrawork/', ConstructorExtraWorkAPIView.as_view()),
    # path('extramaterial/', ConstructorExtraMaterialAPIView.as_view()),

    path('category/equipment/', ConstructorEquipmentAPIView.as_view()),
    path('category/low-tides/', ConstructorLowTidesAPIView.as_view()),
    path('category/lamination/', ConstructorLaminationsAPIView.as_view()),
    path('category/additional-option/', ConstructorAdditionOptionAPIView.as_view()),
    path('category/material/', ConstructorMaterialAPIView.as_view()),

]
