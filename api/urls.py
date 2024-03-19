from django.urls import include, path

urlpatterns = [
    path("brand/", include("api.brand.urls")),
    path("car/", include("api.car.urls")),
]
