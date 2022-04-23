from django.db import models
from apps.core.models import TimestampMixin


class Pet(TimestampMixin):
    class Type(models.TextChoices):
        DOG = 'dog', 'Dog'
        CAT = 'cat', 'Cat'
        RABBIT = 'rabbit', 'Rabbit'
        BIRD = 'bird', 'Bird'
        RODENT = 'rodent', 'Rodent'

    class Size(models.TextChoices):
        SMALL = 'small', 'Small'
        MEDIUM = 'medium', 'Medium'
        LARGE = 'large', 'Large'

    class Meta:
        db_table = 'pets'
        default_related_name = 'pets'

    name = models.TextField(max_length=100)
    type = models.TextField(max_length=20, choices=Type.choices)
    size = models.TextField(max_length=20, choices=Size.choices)
    owner = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)'.format(self.name, self.type)
