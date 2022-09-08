from django.urls import path, include

from .views import CaclulationViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', CaclulationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
