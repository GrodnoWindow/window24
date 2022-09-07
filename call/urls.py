from django.urls import path, include

from .views import *

from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'', CallViewSet) # all routers


urlpatterns = [
    path('', include(router.urls)),
    # path(r'', CallAPIList.as_view()),
    # path(r'', CallViewSet.as_view({'get':'list'})),
    # path(r'<int:pk>/', CallViewSet.as_view({'put':'update'})),
    # path(r'<int:pk>/', ClientAPIView.as_view()),

]
