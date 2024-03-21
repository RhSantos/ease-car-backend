from rest_framework import serializers

from .models import Address, Brand, Car, Rental, Review


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


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "city",
            "state",
            "postal_code",
            "country",
            "complement",
        ]


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = [
            "id",
            "renter",
            "car",
            "created_at",
            "updated_at",
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "reviewer",
            "rental",
            "stars",
            "comment",
            "created_at",
            "updated_at",
        ]