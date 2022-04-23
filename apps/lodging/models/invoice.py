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

    # TODO: Add Invoice model fields




