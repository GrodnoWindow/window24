from django.urls import path, include

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'constructor', ConstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('constructor/', ConstructorAPIList.as_view()),
]
