from django.contrib import admin
from .models import *




# @admin.register(Fittings)
# class FittingsAdmin(admin.ModelAdmin):
#     fields = ['', 'price', 'discount']


admin.site.register(Constructor)
admin.site.register(Profile)
admin.site.register(Fittings)
admin.site.register(ProductType)
admin.site.register(Aggregate)
admin.site.register(SealOutside)
admin.site.register(SealRebate)
admin.site.register(SealInternal)
admin.site.register(SealColor)
admin.site.register(Shpros)
admin.site.register(Shtapik)
admin.site.register(Sash)
admin.site.register(LaminationOutside)
admin.site.register(LaminationInside)
admin.site.register(ProfileWeight)
admin.site.register(Note)
admin.site.register(SupplyValve)

# EXTRAWORKS
admin.site.register(ProductsInstall)
admin.site.register(PvcSlopes)
admin.site.register(FreePositions)

# EXTRAMATERIALS

admin.site.register(FavoritePositions)
admin.site.register(Windowsill)
admin.site.register(WindowsillColor)
admin.site.register(WindowsillType)
# admin.site.register(WindowsillDankeKomfort)
# admin.site.register(WindowsillDankeStandart)
# admin.site.register(WindowsillDankePremium)
admin.site.register(LowTides)
admin.site.register(Visors)
admin.site.register(Flashing)
admin.site.register(FlashingMetal)
admin.site.register(Platband)
admin.site.register(ExtensionsToProfile60)
admin.site.register(ExtensionsToProfile70)
admin.site.register(BayWindowToProfile60)
admin.site.register(BayWindowToProfile70)
admin.site.register(Connector90g)
admin.site.register(Accessories)
admin.site.register(Handles)
admin.site.register(Locks)
admin.site.register(StraightConnectors)
