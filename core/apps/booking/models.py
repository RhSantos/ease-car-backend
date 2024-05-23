from django.db import models
from django.utils import timezone

from core.apps.address.models import Address
from core.apps.authentication.models import ProfileUser
from core.apps.payment.models import Payment
from core.apps.rental.models import Rental


class Booking(models.Model):

    renter = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    rent_date = models.DateTimeField()
    return_date = models.DateTimeField()
    payments = models.ManyToManyField(Payment)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} [{self.renter} - {self.rental}]"
