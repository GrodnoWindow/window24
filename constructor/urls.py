from django.urls import path, include

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', ConstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', ConstructorCreateApi.as_view()),
    path('fields/', FiltersView.as_view()),
]
