from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'', ConstructorViewSet)

urlpatterns = [
    path('window/', ConstructorWindowAPIView.as_view()),
    path('extrawork/', ConstructorExtraWorkAPIView.as_view()),
    path('extramaterial/', ConstructorExtraMaterialAPIView.as_view()),
    path('', include(router.urls)),


]
