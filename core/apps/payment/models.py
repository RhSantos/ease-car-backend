from django.contrib.auth.hashers import make_password as make_hash
from django.db import models
from django.utils import timezone

from core.apps.authentication.models import ProfileUser


class SubAccount(models.Model):
    class IncomeRange(models.TextChoices):
        UP_TO_5K = "UP_TO_5K"
        FROM_5K_TO_10K = "FROM_5K_TO_10K"
        FROM_10K_TO_20K = "FROM_10K_TO_20K"
        ABOVE_20K = "ABOVE_20K"
        UP_TO_50K = "UP_TO_50K"
        FROM_50K_TO_100K = "FROM_50K_TO_100K"
        FROM_100K_TO_250K = "FROM_100K_TO_250K"
        FROM_250K_TO_1MM = "FROM_250K_TO_1MM"
        FROM_1MM_TO_5MM = "FROM_1MM_TO_5MM"
        ABOVE_5MM = "ABOVE_5MM"

    id = models.UUIDField(primary_key=True, editable=False)
    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    income_value = models.DecimalField(max_digits=10, decimal_places=2)
    income_range = models.CharField(max_length=20, choices=IncomeRange.choices)
    api_key = models.CharField(max_length=256)
    wallet_id = models.CharField(max_length=256)
    account_agency = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    account_digit = models.CharField(max_length=2)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Owner: {self.owner}"

    def save(self, *args, **kwargs):
        self.api_key = make_hash(self.api_key)
        self.updated_at = timezone.now()
        super(SubAccount, self).save(*args, **kwargs)


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=30, editable=False)
    person = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    is_notification_disabled = models.BooleanField(default=False)
    observations = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.person)

    def __eq__(self, value: object) -> bool:
        return isinstance(value, type(self)) and self.person == value.person

    def __hash__(self) -> int:
        return hash(self.person)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Customer, self).save(*args, **kwargs)
