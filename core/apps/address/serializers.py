from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "province",
            "city",
            "state",
            "postal_code",
            "country",
            "complement",
        ]
