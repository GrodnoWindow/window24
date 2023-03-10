"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Django
    path('api/users/', include('users.urls')), # Django

    path('api/shema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('api/', include('users.urls')),
    path('api/clients/', include('client.urls')),
    path('api/diary/', include('diary.urls')),
    path('api/miscalculation/', include('miscalculation.urls')),
    path('api/complaint/', include('complaint.urls')),
    path('api/call/', include('call.urls')) ,
    path('api/', include('constructor.urls')),
    path('api/', include('calculation.urls')),
    path('api/correspondence/', include('correspondence.urls')),
    path('api/calls-table/', include('calls_table.urls')),
    path('api/new-call/', include('new_call.urls')),
    path('', include('measurer_window.urls')),
    path('r2d2/', include('measurer_window.urls')),

]