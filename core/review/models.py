from django.db import models
from django.utils import timezone

from core.authentication.models import ProfileUser
from core.rental.models import Rental


class Review(models.Model):

    reviewer = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    stars = models.DecimalField(max_length=2, decimal_places=1, max_digits=2)
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.reviewer} [{self.rental}]"
