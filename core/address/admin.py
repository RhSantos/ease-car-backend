from django.contrib import admin

from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Address._meta.fields]
    parent_fields = Address.get_deferred_fields(Address)

    list_display = all_fields
    read_only = parent_fields
