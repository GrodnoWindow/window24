from django.urls import path, include
from .views import *

urlpatterns = [
    path('window/', ConstructorWindowAPIView.as_view()),
    path('extrawork/', ConstructorExtraWorkAPIView.as_view()),
    path('extramaterial/', ConstructorExtraMaterialAPIView.as_view()),

]
