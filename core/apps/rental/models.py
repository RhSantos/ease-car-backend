from django.db import models
from core.apps.authentication.models import ProfileUser
from core.apps.car.models import Car
from django.utils import timezone

class Rental(models.Model):
    class RentType(models.TextChoices):
        DAILY = "Daily"
        WEEKLY = "Weekly"
        MONTHLY = "Monthly"
        YEARLY = "Yearly"

    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rent_type = models.CharField(
        max_length=20, choices=RentType.choices, default=RentType.WEEKLY
    )
    rent_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner} - {self.car}"

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Rental, self).save(*args, **kwargs)
