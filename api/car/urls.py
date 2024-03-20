from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_cars, name="get_all_cars"),
    path("<int:car_id>/", views.get_car, name="get_car"),
]
