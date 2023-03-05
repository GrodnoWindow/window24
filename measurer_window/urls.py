from django.urls import path, include

from .views import *
from rest_framework import routers


urlpatterns = [
    path('', home),
    # path('<int:pk>/', OrderDetailView.as_view(), name="order_list"),
    path('<int:pk>/', order),

    # path('', MiscalculationAPIList.as_view()),

    # path('home/', include('users.urls')),

]
