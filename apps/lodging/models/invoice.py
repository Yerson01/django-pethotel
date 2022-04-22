from django.db import models

from apps.core.models import TimestampMixin


class Invoice(TimestampMixin):
    class Status(models.TextChoices):
        SENT = 'sent', 'Sent'
        PAID = 'paid', 'Paid'
        OVERDUE = 'overdue', 'Overdue'

    class Meta:
        db_table = 'invoices'
        default_related_name = 'invoices'

    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    status = models.TextField(max_length=30, choices=Status.choices)




