from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe

from core.apps.address.models import Address
from core.general.managers import ProfileUserManager


class ProfileUser(AbstractUser):
    profile_pic = models.ImageField(upload_to="user/")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    birth_date = models.DateField(verbose_name="Birth Date")
    mobile_phone = models.CharField(max_length=12, verbose_name="Mobile Phone")
    is_premium = models.BooleanField(default=False)

    REQUIRED_FIELDS = [
        "email",
        "first_name",
        "last_name",
        "cpf",
        "birth_date",
        "mobile_phone",
    ]

    objects = ProfileUserManager()

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, type(self))
            and self.email == value.email
            and self.cpf == value.cpf
        )

    def __hash__(self) -> int:
        return hash(tuple(self.email, self.cpf))

    def thumbnail(self):
        img_url = self.profile_pic.url if self.profile_pic else ""
        return mark_safe('<img src="%s" height="80px"/>' % img_url)

    thumbnail.allow_tags = True
