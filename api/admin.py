from django.contrib import admin

from .models import Brand, Car, Address


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ["name", "image_preview", "image"]
    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Address._meta.fields]
    parent_fields = Address.get_deferred_fields(Address)

    list_display = all_fields
    read_only = parent_fields