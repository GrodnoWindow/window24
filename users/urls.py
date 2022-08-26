from django.urls import path
from .views import *
urlpatterns = [
    path('users', users),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view()),
]