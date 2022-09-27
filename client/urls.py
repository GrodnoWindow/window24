from django.urls import path, include

from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'',ClientViewSet)
urlpatterns = [

    path('',include(router.urls)),
    path('create', ClientAPIView.as_view())
    # path(r'all/', ClientGenericAPIView.as_view()),


]
