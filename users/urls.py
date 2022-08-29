from django.urls import path
from .views import *
urlpatterns = [
    path('register', UserRegister.as_view()),
    path('login', UserLogin.as_view()),
    path('logout', logout),
    path('user', AuthenticatedUser.as_view()),
    path('permissions', PermissionAPIView.as_view()),
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
    })),
    path('users', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view())
]
