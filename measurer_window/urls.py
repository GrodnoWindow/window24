from django.urls import path, include

from .views import *
from rest_framework import routers


urlpatterns = [
    path('', home),
    # path('<int:pk>/', OrderDetailView.as_view(), name="order_list"),
    # path('<int:pk>/', order, name='order'),
    path('<int:pk>/<slug:form>/', order, name='order'),
    path('accounts/', include('django.contrib.auth.urls')),

    # path('', MiscalculationAPIList.as_view()),

    # path('home/', include('users.urls')),

]
