from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]
