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

    def to_representation(self, data):
        data = super(RegisterSerializer, self).to_representation(data)
        data["address"] = Address.objects.filter(id=data["address"]).values()
        return data
