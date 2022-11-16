from django.urls import path, include

from .views import *
from rest_framework import routers

router_number = routers.SimpleRouter()
# router_number.register(r'number', NumberViewSet)

router_address = routers.SimpleRouter()
# router_address.register(r'address', AddressViewSet)

router = routers.SimpleRouter()
# router.register(r'',ClientViewSet)
urlpatterns = [

    path('', ClientViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', ClientViewSet.as_view({'get': 'retrieve'})),
    path('update/<int:pk>/', ClientPatchAPIView.as_view()),
    path('add', ClientAPIView.as_view()),

    path('address', AddressViewSet.as_view({'get': 'list'})),
    path('address/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'})),
    path('address/update/<int:pk>/', AddressViewSet.as_view({'patch': 'update'})),
    path('address/add', AddressViewSet.as_view({'post': 'create'})),

    path('number', NumberViewSet.as_view({'get': 'list'})),
    path('number/<int:pk>/', NumberViewSet.as_view({'get': 'retrieve'})),
    path('number/update/<int:pk>/', NumberViewSet.as_view({'patch': 'update'})),
    path('number/add', NumberViewSet.as_view({'post': 'create'})),


]
