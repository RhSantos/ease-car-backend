from django.contrib.auth.models import BaseUserManager
from django.db import models


class ProfileUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        profile_user = self.model(email=email, **extra_fields)
        profile_user.set_password(password)
        profile_user.profile_pic = extra_fields.get("profile_pic")
        profile_user.address = extra_fields.get("address")
        profile_user.save(using=self._db)
        return profile_user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50, default="Brasil")
    complement = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"
