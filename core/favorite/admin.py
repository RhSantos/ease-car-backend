from django.contrib import admin

from .models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Favorite._meta.fields]
    parent_fields = Favorite.get_deferred_fields(Favorite)

    list_display = all_fields
    read_only = parent_fields
