from django.contrib import admin
from .models import *


@admin.register(Price)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['price', 'discount']
    list_display = ['price', 'discount']


admin.site.register(ProductType)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['profile_name', 'price']
    list_display = ['profile_name', 'get_price']


admin.site.register(Aggregate)


@admin.register(Fittings)
class FittingsAdmin(admin.ModelAdmin):
    fields = ['fittings', 'price']
    list_display = ['fittings', 'get_price']


admin.site.register(SealOutside)
admin.site.register(SealRebate)
admin.site.register(SealInternal)
admin.site.register(Lock)
admin.site.register(Shpros)
admin.site.register(Shtapik)
admin.site.register(Sash)
admin.site.register(Lamination_outside)
admin.site.register(Lamination_inside)
admin.site.register(Profile_weight)
admin.site.register(Note)

# EXTRAWORKS
admin.site.register(Products_install)
admin.site.register(Pvc_slopes)
admin.site.register(Free_positions)

# EXTRAMATERIALS

admin.site.register(Favorite_positions)
admin.site.register(Windowsill)
admin.site.register(Windowsill_danke_komfort)
admin.site.register(Windowsill_danke_standart)
admin.site.register(Windowsill_danke_premium)
admin.site.register(Low_tides)
admin.site.register(Visors)
admin.site.register(Flashing)
admin.site.register(Flashing_metal)
admin.site.register(Platband)
admin.site.register(Extensions_to_profile_sixty)
admin.site.register(Extensions_to_profile_seventy)
admin.site.register(Bay_window_to_profile_sixty)
admin.site.register(Bay_window_to_profile_seventy)
admin.site.register(Connector_90g)
admin.site.register(Accessories)
admin.site.register(Handles_and_locks)
admin.site.register(Straight_connectors)
