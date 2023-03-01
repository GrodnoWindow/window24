from django.urls import path, include

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', MeasurementViewSet) # all routers

urlpatterns = [
    path('', index),
    # path('', MiscalculationAPIList.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('record/', include(router.urls)),

    # path('home/', include('users.urls')),

]
