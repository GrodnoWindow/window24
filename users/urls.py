from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from django.urls import path,include

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', register),

    path('user', AuthenticatedUser.as_view()),

    path('users', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view()),

    path("signup/", SignUp.as_view(), name="signup"),
]
