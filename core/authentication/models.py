from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.safestring import mark_safe


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


class ProfileUser(AbstractUser):
    profile_pic = models.ImageField(upload_to="user/")
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )

    REQUIRED_FIELDS = ["email"]

    objects = ProfileUserManager()

    def thumbnail(self):
        img_url = self.profile_pic.url if self.profile_pic else ""
        return mark_safe('<img src="%s" height="80px"/>' % img_url)

    thumbnail.allow_tags = True
