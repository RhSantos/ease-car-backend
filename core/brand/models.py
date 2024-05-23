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
