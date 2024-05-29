from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    province = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50, default="Brasil")
    complement = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}, {self.country}"
