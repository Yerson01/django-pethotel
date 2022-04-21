from django.db import models
from apps.core.models.mixins import TimestampMixin


class Room(models.Model, TimestampMixin):
    class Meta:
        default_related_name = 'rooms'

    room_number = models.IntegerField(max_length=5)
    cost_per_night = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.room_number)