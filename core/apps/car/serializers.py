from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "name",
            "image",
            "model_year",
            "brand",
            "passengers",
            "doors",
            "has_air_conditioning",
            "has_power_locks",
            "has_power_windows",
            "fuel_type",
            "is_automatic",
            "horsepower",
            "top_speed",
            "acceleration_0_100",
        ]
