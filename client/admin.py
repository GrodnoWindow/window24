from django.contrib import admin
from .models import Client



admin.site.register(Client)


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     filter_horizontal = ['calls']