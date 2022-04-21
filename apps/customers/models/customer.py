from django.contrib.auth.models import User
from apps.core.models.mixins import TimestampMixin


class Customer(User, TimestampMixin):

    class Meta:
        proxy = True
        default_related_name = 'customers'

    def __str__(self):
        return self.email
    
    