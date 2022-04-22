from django.contrib import admin

from apps.lodging.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fields = ('room_number', 'cost_per_night',)
    list_display = ('id', 'room_number', 'cost_per_night')
    list_display_links = ('id', 'room_number')
