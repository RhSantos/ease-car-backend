from rest_framework import serializers

from .models import Address, ProfileUser


class RegisterSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    class Meta:
        model = ProfileUser
        fields = [
            "id",
            "email",
            "password",
            "username",
            "first_name",
            "last_name",
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
        except:
            data["address"] = None
        return data