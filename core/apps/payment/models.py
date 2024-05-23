import hashlib
import uuid

from django.db import models
from django.utils import timezone

from core.apps.authentication.models import ProfileUser


class Payment(models.Model):

    class Type(models.TextChoices):
        CREDIT_CARD = "Credit Card"
        DEBIT_CARD = "Debit Card"
        CASH = "Cash"

    class Status(models.TextChoices):
        PENDING = "Pending"
        COMPLETED = "Completed"
        CANCELLED = "Cancelled"
        FAILED = "Failed"

    owner = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE, related_name="payment_owner"
    )
    receiver = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE, related_name="payment_receiver"
    )

    payment_type = models.CharField(
        max_length=20, choices=Type.choices, default=Type.CREDIT_CARD
    )
    payment_hash = models.CharField(
        primary_key=True,
        max_length=100,
        editable=False,
    )
    payment_status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    bill_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment HASH: {self.payment_hash}"

    def save(self, *args, **kwargs):
        if not self.payment_hash:
            self.payment_hash = hashlib.sha256(uuid.uuid4().bytes).hexdigest()
        self.updated_at = timezone.now()
        super(Payment, self).save(*args, **kwargs)
