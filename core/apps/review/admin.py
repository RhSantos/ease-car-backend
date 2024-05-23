from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Review._meta.fields]
    parent_fields = Review.get_deferred_fields(Review)

    list_display = all_fields
    read_only = parent_fields
