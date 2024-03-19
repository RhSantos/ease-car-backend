from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand_images/')

