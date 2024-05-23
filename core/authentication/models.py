from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from core.general.managers import ProfileUserManager

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
