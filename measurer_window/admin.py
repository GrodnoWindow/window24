from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Status)
admin.site.register(WindowsillWidth)
admin.site.register(Unit)

admin.site.register(Windowsill)
admin.site.register(WindowsillCalc)
admin.site.register(WindowsillComplectCalc)

admin.site.register(LowTides)
admin.site.register(LowTidesCalc)
admin.site.register(LowTidesComplectCalc)

admin.site.register(Visors)
admin.site.register(VisorsCalc)


admin.site.register(Flashing)
admin.site.register(FlashingCalc)


admin.site.register(Casing)
admin.site.register(CasingCalc)

admin.site.register(SlopesOfMetal)
admin.site.register(SlopesOfMetalCalc)

admin.site.register(InternalSlopes)
admin.site.register(InternalSlopesCalc)

admin.site.register(MountingMaterials)
admin.site.register(MountingMaterialsCalc)

admin.site.register(Order)