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
    path('api/', include('users.urls')), # Django

    path('api/shema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('api/', include('users.urls')),
    path('clients/', include('client.urls')),
    path('diary/', include('diary.urls')),
    path('miscalculation/', include('miscalculation.urls')),
    path('complaint/', include('complaint.urls')),
    path('call/', include('call.urls')),
    path('', include('constructor.urls')),
    path('', include('calculation.urls')),
    path('correspondence/', include('correspondence.urls')),
    path('calls-table/', include('calls_table.urls')),
    path('measurer/', include('measurer_window.urls')),
    path('new-call/', include('new_call.urls')),
    path('r2d2/', include('measurer_window.urls')),

]