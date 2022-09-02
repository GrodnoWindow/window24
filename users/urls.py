from django.urls import path

from .views import *
urlpatterns = [

    path('register', register),
    path('curent_user', AuthenticatedUser.as_view()),
    path('permissions', PermissionAPIView.as_view()),
    path('users', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view()),
]
