from django.urls import path, include

from .views import *
from rest_framework import routers

urlpatterns = [
    path('', index),
    # path('', MiscalculationAPIList.as_view()),
]
