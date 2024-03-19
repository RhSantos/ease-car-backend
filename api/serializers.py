from rest_framework import serializers

from .models import Brand, Car


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "image"]

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "name",
            "brand",
            "passengers",
            "doors",
            "has_air_conditioning",
            "has_power_locks",
            "has_power_windows",
            "fuel_type",
            "is_manual",
            "horsepower",
            "top_speed",
            "acceleration_0_100",
        ]
