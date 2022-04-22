from apps.core.models import User


class Customer(User):

    class Meta:
        proxy = True
        default_related_name = 'customers'

    def __str__(self):
        return self.email
    
    