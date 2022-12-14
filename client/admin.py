from django.contrib import admin
from .models import Client, Number, Address, Prompter

admin.site.register(Client)
admin.site.register(Number)
admin.site.register(Address)
admin.site.register(Prompter)


