from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .brand.views import BrandViewSet
from .car.views import CarViewSet

router = DefaultRouter()
router.register("car", CarViewSet)
router.register("brand", BrandViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
