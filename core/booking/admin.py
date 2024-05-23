from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Booking._meta.fields]
    parent_fields = Booking.get_deferred_fields(Booking)

    list_display = all_fields
    read_only = parent_fields
