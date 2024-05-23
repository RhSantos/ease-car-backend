from rest_framework import serializers

from .models import Payment


class PaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "owner",
            "receiver",
            "payment_type",
            "amount",
            "description",
            "bill_date",
        ]


class PaymentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "payment_hash",
            "owner",
            "receiver",
            "payment_type",
            "payment_status",
            "amount",
            "description",
            "bill_date",
            "created_at",
            "updated_at",
        ]
