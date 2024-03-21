from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .routes.address.views import AddressViewSet
from .routes.brand.views import BrandViewSet
from .routes.car.views import CarViewSet
from .routes.rental.views import RentalViewSet
from .routes.review.views import ReviewViewSet

router = DefaultRouter()
router.register("car", CarViewSet)
router.register("brand", BrandViewSet)
router.register("address", AddressViewSet)
router.register("rental", RentalViewSet)
router.register("review", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
