from django.urls import path, include

from client.views import *


urlpatterns = [

    # path('/all/', ClientAPIViewAll.as_view()),
    path('all/', ClientAPIList.as_view()),
    path('<int:pk>/', ClientAPIView.as_view()),

]
