from django.urls import path, include

from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet) # all routers


urlpatterns = [
    # path('', TaskAPIList.as_view()),
    # path(r'overdue=<slug:slug>', TaskAPIList.as_view()),
    path('', include(router.urls)),
    path('tasks/', TaskAPIList.as_view()),
]
