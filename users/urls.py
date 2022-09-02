from django.urls import path

from .views import *
urlpatterns = [

    path('register', register),
    path('curent_user', AuthenticatedUser.as_view()),
    path('permissions', PermissionAPIView.as_view()),
    path('roles', GroupViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', GroupViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
    })),
    path('users', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view()),
]
