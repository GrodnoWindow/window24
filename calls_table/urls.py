from django.urls import path, include

from .views import *

from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'', CallView) # all routers
router_call = routers.SimpleRouter()
router_call.register(r'', OutgoingCallViewSet) # all routers


urlpatterns = [
    # path('', include(router.urls)),
    # path(r'active/', CallView.as_view()),
    path('', include(router_call.urls)),

    path(r'', CallsTableGenericAPIView.as_view()),

    # path(r'<int:pk>/', CallsTableAPIView.as_view()),
    # path(r'all', CallAllView.as_view()),
    # path(r'', CallViewSet.as_view({'get':'list'})),
    # path(r'<int:pk>/', CallViewSet.as_view({'put':'update'})),
    # path(r'<int:pk>/', ClientAPIView.as_view()),

]
