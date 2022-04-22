from django.db import models


class Room(models.Model):
    class Meta:
        db_table = 'rooms'
        default_related_name = 'rooms'

    room_number = models.IntegerField()
    cost_per_night = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.room_number)
