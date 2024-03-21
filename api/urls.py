from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .address.views import AddressViewSet
from .brand.views import BrandViewSet
from .car.views import CarViewSet
from .rental.views import RentalViewSet

router = DefaultRouter()
router.register("car", CarViewSet)
router.register("brand", BrandViewSet)
router.register("address", AddressViewSet)
router.register("rental", RentalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
