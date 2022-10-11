from django.contrib import admin
from .models import Client, Number, Address

admin.site.register(Client)
admin.site.register(Number)
admin.site.register(Address)

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     filter_horizontal = ['calls']
