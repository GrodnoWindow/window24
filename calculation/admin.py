from django.contrib import admin
from .models import *

admin.site.register(WindowDiscountMarkups)
admin.site.register(ExchangeRates)
admin.site.register(WindowsillCalc)

admin.site.register(WindowsCalc)
admin.site.register(LowTidesCalc)
admin.site.register(Constructor)
admin.site.register(FlashingCalc)
admin.site.register(CasingCalc)

# markups
admin.site.register(Windowsill_Markups)
admin.site.register(LowTides_Markups)
admin.site.register(Casing_Markups)
admin.site.register(Flashing_Markups)
admin.site.register(Visors_Markups)