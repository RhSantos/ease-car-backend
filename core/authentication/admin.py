from django.contrib import admin

from .models import ProfileUser


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "first_name", "last_name", "profile_pic", "address"]
    list_display = ["id", "thumbnail", "username", "email"]
