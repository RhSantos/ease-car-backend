from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .address.views import AddressViewSet
from .brand.views import BrandViewSet
from .car.views import CarViewSet

router = DefaultRouter()
router.register("car", CarViewSet)
router.register("brand", BrandViewSet)
router.register("address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
