from django.db import models
from apps.core.models import TimestampMixin


class Booking(TimestampMixin):
    class Status(models.TextChoices):
        BOOKED = 'booked', 'Booked'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    status = models.TextField(max_length=30, choices=Status.choices)
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    fee = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Booking %s' % self.id

