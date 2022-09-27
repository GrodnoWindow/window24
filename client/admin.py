from django.contrib import admin
from .models import Client,Number



admin.site.register(Client)
admin.site.register(Number)


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     filter_horizontal = ['calls']