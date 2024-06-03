from rest_framework import serializers

from .models import Customer, SubAccount, Subscription


class SubAccountRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubAccount
        fields = [
            "id",
            "owner",
            "income_value",
            "created_at",
            "updated_at",
        ]


class SubAccountResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubAccount
        fields = [
            "id",
            "owner",
            "income_value",
            "income_range",
            "api_key",
            "wallet_id",
            "account_agency",
            "account_number",
            "account_digit",
            "created_at",
            "updated_at",
        ]


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "id",
            "person",
            "is_notification_disabled",
            "observations",
            "created_at",
            "updated_at",
        ]


class SubscriptionRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            "id",
            "customer",
            "billing_type",
            "value",
            "next_due_date",
            "discount_percentage",
            "interest_value",
            "fine_value",
            "cycle",
            "description",
            "end_date",
            "created_at",
            "updated_at",
        ]


class SubscriptionResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            "id",
            "customer",
            "billing_type",
            "cycle",
            "value",
            "next_due_date",
            "end_date",
            "description",
            "status",
            "discount_percentage",
            "fine_value",
            "interest_value",
            "created_at",
            "updated_at",
        ]
