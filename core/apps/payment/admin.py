from django.contrib import admin

from .models import SubAccount, Customer


@admin.register(SubAccount)
class SubAccountAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in SubAccount._meta.fields]
    parent_fields = SubAccount.get_deferred_fields(SubAccount)

    list_display = all_fields
    read_only = parent_fields

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Customer._meta.fields]
    parent_fields = Customer.get_deferred_fields(Customer)

    list_display = all_fields
    read_only = parent_fields