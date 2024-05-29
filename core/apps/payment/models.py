import uuid

from django.db import models
from django.utils import timezone

from core.apps.authentication.models import ProfileUser
from django.contrib.auth.hashers import make_password as make_hash

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
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    income_value = models.DecimalField(max_digits=10,decimal_places=2)
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
