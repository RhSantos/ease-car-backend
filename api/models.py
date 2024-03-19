from django.db import models
from django.utils.safestring import mark_safe


class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="brand/")

    def __str__(self):
        return self.name

    def image_preview(self):
        return mark_safe('<img src="%s"/>' % self.image.url)

    image_preview.allow_tags = True


class Car(models.Model):

    class FuelTypes(models.TextChoices):
        GASOLINE = "Gasoline"
        DIESEL = "Diesel"
        PROPANE = "Propane"
        CNG = "CNG"
        ETHANOL = "Ethanol"
        BIODIESEL = "Bio-diesel"

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="car/")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    passengers = models.IntegerField()
    doors = models.IntegerField()
    has_air_conditioning = models.BooleanField()
    has_power_locks = models.BooleanField()
    has_power_windows = models.BooleanField()
    fuel_type = models.CharField(
        max_length=20,
        choices=FuelTypes.choices,
        default=FuelTypes.GASOLINE,
    )
    is_automatic = models.BooleanField()
    horsepower = models.IntegerField()
    top_speed = models.IntegerField()
    acceleration_0_100 = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name + f"({self.brand.name})"

    def image_preview(self):
        return mark_safe('<img src="%s" height="200px"/>' % self.image.url)

    image_preview.allow_tags = True
