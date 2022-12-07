from django.urls import path, include

from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'', MiscalculationViewSet) # all routers


urlpatterns = [
    path('', include(router.urls)),
    path('', MiscalculationAPIList.as_view()),
]
