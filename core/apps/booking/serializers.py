from datetime import datetime, timedelta
from math import ceil

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.apps.address.serializers import AddressSerializer
from core.apps.payment.models import SubAccount
from core.apps.rental.models import Rental
from core.apps.rental.serializers import RentalSerializer

from .models import Booking


class BookingRequestSerializer(serializers.ModelSerializer):
    rental = RentalSerializer()
    location = AddressSerializer()

    class Meta:
        model = Booking
        fields = [
            "renter",
            "rental",
            "location",
            "rent_date",
            "return_date",
            "created_at",
            "updated_at",
        ]


class BookingResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "renter",
            "rental",
            "location",
            "rent_date",
            "return_date",
            "created_at",
            "updated_at",
        ]
