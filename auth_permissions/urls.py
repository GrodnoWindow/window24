from django.urls import path
from .views import *

urlpatterns = [
    path('permission/<int:pk>/', PermissionDetail.as_view()),
    path('permission/', PermissionList.as_view()),
]
