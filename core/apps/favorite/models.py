from django.db import models
from django.utils import timezone

from core.apps.authentication.models import ProfileUser
from core.apps.rental.models import Rental


class Favorite(models.Model):

    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Favorite, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} [{self.rental}]"
