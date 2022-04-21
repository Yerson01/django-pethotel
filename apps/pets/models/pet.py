from django.db import models
from apps.core.models.mixins import TimestampMixin


class Pet(models.Model, TimestampMixin):
    class Meta:
        default_related_name = 'pets'

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

    name = models.TextField(max_length=100)
    type = models.TextField(max_length=20, choices=Type.choices)
    size = models.TextField(max_length=20, choices=Type.choices)
    owner = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)'.format(self.name, self.type)
