from django.contrib import admin

from .models import Customer, SubAccount, Subscription


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


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    all_fields = [f.name for f in Subscription._meta.fields]
    parent_fields = Subscription.get_deferred_fields(Subscription)

    list_display = all_fields
    read_only = parent_fields
