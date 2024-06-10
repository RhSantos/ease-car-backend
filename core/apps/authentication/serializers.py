from rest_framework import serializers

from core.apps.address.models import Address

from .models import ProfileUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = ProfileUser
        fields = [
            "id",
            "email",
            "password",
            "username",
            "first_name",
            "last_name",
            "cpf",
            "birth_date",
            "mobile_phone",
            "is_premium",
            "address",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = ProfileUser.objects.create_user(**validated_data)
        return user

    def to_representation(self, data):
        data = super(RegisterSerializer, self).to_representation(data)
        try:
            data["address"] = Address.objects.filter(id=data["address"]).values()[0]
        except IndexError:
            data["address"] = None
        return data


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileUser
        fields = [
            "id",
            "email",
            "password",
        ]

        extra_kwargs = {"password": {"write_only": True}}
