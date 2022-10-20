from django.urls import path, include

from .views import *
from rest_framework import routers

router_number = routers.SimpleRouter()
router_number.register(r'number', NumberViewSet)

router_address = routers.SimpleRouter()
router_address.register(r'address', AddressViewSet)

router = routers.SimpleRouter()
router.register(r'all',ClientViewSet)
urlpatterns = [

    path('',include(router.urls)),
    path('',include(router_number.urls)),
    path('',include(router_address.urls)),
    path('', ClientAPIView.as_view()),
    # path('all', ClientsRecordsView.as_view()),
    # path(r'all/', ClientGenericAPIView.as_view()),


]
