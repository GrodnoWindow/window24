from django.urls import path
from .views import *

urlpatterns = [
    # rest-framework
    path('group/<int:pk>/', GroupDetail.as_view()),
    path('group/', GroupList.as_view()),
]
