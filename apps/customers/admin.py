from django.contrib import admin

from apps.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email', 'phone_number',)
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'first_name')
