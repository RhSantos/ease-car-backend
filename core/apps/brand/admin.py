from django.contrib import admin

from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ["name", "image_preview", "image"]
    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]
