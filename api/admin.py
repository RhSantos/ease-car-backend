from django.contrib import admin

from .models import Address, Brand, Car, Favorite, Rental, Review


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


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Rental._meta.fields]
    parent_fields = Rental.get_deferred_fields(Rental)

    list_display = all_fields
    read_only = parent_fields


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Review._meta.fields]
    parent_fields = Review.get_deferred_fields(Review)

    list_display = all_fields
    read_only = parent_fields


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Favorite._meta.fields]
    parent_fields = Favorite.get_deferred_fields(Favorite)

    list_display = all_fields
    read_only = parent_fields
