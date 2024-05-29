from rest_framework import serializers

from .models import SubAccount


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
