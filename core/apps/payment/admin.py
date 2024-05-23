from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Payment._meta.fields]
    parent_fields = Payment.get_deferred_fields(Payment)

    list_display = all_fields
    read_only = parent_fields
