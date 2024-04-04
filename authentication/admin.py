from django.contrib import admin

from .models import Address, ProfileUser


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Address._meta.fields]
    parent_fields = Address.get_deferred_fields(Address)

    list_display = all_fields
    read_only = parent_fields


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "first_name", "last_name", "profile_pic", "address"]
    list_display = ["id", "thumbnail", "username", "email"]
