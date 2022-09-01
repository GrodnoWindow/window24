from django.urls import path, include

from diary.views import *


urlpatterns = [
    path('', TaskAPIList.as_view()),
    path(r'overdue=<slug:slug>', TaskAPIList.as_view()),

]
