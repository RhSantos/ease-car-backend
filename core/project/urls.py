from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.apps.address.views import AddressViewSet
from core.apps.authentication.views import (
    LoginViewSet,
    RegisterViewSet,
    TokenRefreshViewSet,
    TokenVerifyViewSet,
)
from core.apps.booking.views import BookingViewSet
from core.apps.brand.views import BrandViewSet
from core.apps.car.views import CarViewSet
from core.apps.favorite.views import FavoriteViewSet
from core.apps.payment.views import CustomerViewSet, SubAccountViewSet
from core.apps.rental.views import RentalViewSet
from core.apps.review.views import ReviewViewSet

router = DefaultRouter()

# Authentication Routes
router.register("auth/register", RegisterViewSet, basename="auth-register")
router.register("auth/login", LoginViewSet, basename="auth-login")
router.register("auth/refresh-token", TokenRefreshViewSet, basename="auth-token")
router.register("auth/verify-token", TokenVerifyViewSet, basename="auth-verify")

# Payment Routes
router.register("payment/customer", CustomerViewSet, basename="payment-customer")
router.register("payment/subaccount", SubAccountViewSet, basename="payment-subaccount")

# Models Routes
router.register("address", AddressViewSet, basename="api-address")
router.register("booking", BookingViewSet, basename="api-booking")
router.register("brand", BrandViewSet, basename="api-brand")
router.register("car", CarViewSet, basename="api-car")
router.register("favorite", FavoriteViewSet, basename="api-favorite")
router.register("rental", RentalViewSet, basename="api-rental")
router.register("review", ReviewViewSet, basename="api-review")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
