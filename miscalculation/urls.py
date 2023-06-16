from django.urls import path, include


from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'', MiscalculationViewSet) # all routers

router_offer = routers.SimpleRouter()
router_offer.register(r'', CommercialOfferViewSet) # all routers

urlpatterns = [
    path('', include(router.urls)),
    path('offer/', include(router_offer.urls)),

]
