from django.contrib import admin

from .models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Rental._meta.fields]
    parent_fields = Rental.get_deferred_fields(Rental)

    list_display = all_fields
    read_only = parent_fields
