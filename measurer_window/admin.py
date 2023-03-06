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

admin.site.register(Order)