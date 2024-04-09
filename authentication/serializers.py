from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.serializers import AddressSerializer

from .models import Address, ProfileUser


class ProfileUserSerializer(serializers.ModelSerializer):
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
        data = super(ProfileUserSerializer, self).to_representation(data)
        data['address'] = Address.objects.filter(id=data['address']).values()
        return data
