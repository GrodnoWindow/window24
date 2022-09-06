from django.urls import path, include

from .views import *


urlpatterns = [

    path(r'', ClientAPIList.as_view()),
    path(r'<int:pk>/', ClientAPIView.as_view()),

]
