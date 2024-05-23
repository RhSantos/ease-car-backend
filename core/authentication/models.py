from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe

from core.address.models import Address
from core.general.managers import ProfileUserManager


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
