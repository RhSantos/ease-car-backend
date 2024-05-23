from datetime import datetime, timedelta
from math import ceil

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.address.serializers import AddressSerializer
from core.payment.models import Payment
from core.rental.models import Rental
from core.rental.serializers import RentalSerializer

from .models import Booking


class BookingRequestSerializer(serializers.ModelSerializer):

    payment_type = serializers.ChoiceField(
        choices=Payment.Type.choices, default=Payment.Type.CREDIT_CARD
    )
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
            "payment_type",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):

        return super().create(validated_data)

    def save(self, **kwargs):
        rental = self.validated_data["rental"]

        try:
            rent_type = Rental.RentType(rental.get("rent_type"))
        except:
            raise ValidationError(_("Wrong Rental Type Argument"))

        rent_value = rental.get("rent_value")

        rent_date = self.validated_data["rent_date"]
        return_date = self.validated_data["return_date"]

        diff: timedelta = return_date - rent_date
        bill_date_days_aggregator = 0

        payment_number = 0

        match rent_type:
            case Rental.RentType.DAILY:

                payment_number = diff.days
                bill_date_days_aggregator = 1

                if payment_number == 0 and diff.seconds >= 3600:
                    payment_number = 1

            case Rental.RentType.WEEKLY:

                payment_number = ceil(diff.days / 7)
                bill_date_days_aggregator = 7

                if payment_number == 0 and diff.days >= 1:
                    payment_number = 1

            case Rental.RentType.MONTHLY:

                payment_number = ceil(diff.days / 30)
                bill_date_days_aggregator = 30

                if payment_number == 0 and diff.days >= 1:
                    payment_number = 1

            case Rental.RentType.YEARLY:

                payment_number = ceil(diff.days / 365)
                bill_date_days_aggregator = 365

                if payment_number == 0 and diff.days >= 1:
                    payment_number = 1

        bill_date: datetime = rent_date + timedelta(days=bill_date_days_aggregator)

        for num in range(payment_number):
            payment = Payment(
                owner=self.validated_data["renter"],
                receiver=rental.get("owner"),
                payment_type=self.validated_data["payment_type"],
                amount=rent_value,
                description=_(
                    f"{num + 1}# {bill_date.strftime('%B')} {bill_date.day}/{bill_date.year}"
                ),
                bill_date=bill_date,
            )
            payment.save()
            bill_date += timedelta(days=bill_date_days_aggregator)

        return super().save(**kwargs)


class BookingResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "renter",
            "rental",
            "location",
            "rent_date",
            "return_date",
            "payments",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, data):
        data = super(BookingResponseSerializer, self).to_representation(data)
        try:
            data["payments"] = [
                Payment.objects.get(id=payment_id) for payment_id in data["payments"]
            ]
        except IndexError:
            data["payments"] = []
        return data
