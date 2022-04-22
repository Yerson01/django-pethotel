from django.db import models
from django.utils import timezone

from apps.core.models import TimestampMixin


class Booking(TimestampMixin):
    class Status(models.TextChoices):
        BOOKED = 'booked', 'Booked'
        IN_PROGRESS = 'In Progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    class Meta:
        db_table = 'bookings'
        default_related_name = 'bookings'

    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()

    # invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking %s' % self.pk

    @property
    def status(self):
        now = timezone.now()

        if self.arrival_date > now:
            return self.Status.BOOKED
        elif self.departure_date > now:
            return self.Status.IN_PROGRESS

        return self.Status.BOOKED
