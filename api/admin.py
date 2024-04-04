from django.contrib import admin

from .models import Booking, Brand, Car, Favorite, Payment, ProfileUser, Rental, Review


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "first_name", "last_name", "profile_pic", "address"]
    list_display = ["id", "thumbnail", "username", "email"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ["name", "image_preview", "image"]
    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]


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


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Payment._meta.fields]
    parent_fields = Payment.get_deferred_fields(Payment)

    list_display = all_fields
    read_only = parent_fields


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Booking._meta.fields]
    parent_fields = Booking.get_deferred_fields(Booking)

    list_display = all_fields
    read_only = parent_fields
