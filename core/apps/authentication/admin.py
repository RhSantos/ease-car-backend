from django.contrib import admin

from .models import ProfileUser


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "email",
        "first_name",
        "last_name",
        "cpf",
        "profile_pic",
        "birth_date",
        "mobile_phone",
        "is_premium",
        "address",
    ]
    list_display = ["id", "thumbnail", "username", "email"]
