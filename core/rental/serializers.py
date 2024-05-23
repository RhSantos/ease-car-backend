from rest_framework import serializers

from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = [
            "id",
            "owner",
            "car",
            "rent_type",
            "rent_value",
            "created_at",
            "updated_at",
        ]
