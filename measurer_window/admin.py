from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Status)
admin.site.register(Unit)

admin.site.register(Windowsill)
admin.site.register(WindowsillWidth)
admin.site.register(WindowsillPlug)
admin.site.register(WindowsillConnection)
admin.site.register(WindowsillCalc)

admin.site.register(LowTides)
admin.site.register(LowTidesType)
admin.site.register(LowTidesColor)
admin.site.register(LowTidesPlug)
admin.site.register(LowTidesConnection)
admin.site.register(LowTidesCalc)

admin.site.register(Visors)
admin.site.register(VisorsColor)
admin.site.register(VisorsCalc)

admin.site.register(Flashing)
admin.site.register(FlashingColor)
admin.site.register(FlashingCalc)

admin.site.register(Casing)
admin.site.register(CasingColor)
admin.site.register(CasingCalc)

admin.site.register(SlopesOfMetal)
admin.site.register(SlopesOfMetalColor)
admin.site.register(SlopesOfMetalCalc)

admin.site.register(InternalSlopes)
admin.site.register(InternalSlopesColor)
admin.site.register(InternalSlopesCalc)

admin.site.register(MountingMaterials)
admin.site.register(MountingMaterialsCalc)

admin.site.register(Works)
admin.site.register(WorksCalc)

admin.site.register(Order)
