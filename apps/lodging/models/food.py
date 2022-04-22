from django.db import models


class Food(models.Model):
    class Type(models.TextChoices):
        BREAKFAST = 'breakfast', 'Breakfast'
        LUNCH = 'lunch', 'Lunch'
        DINNER = 'dinner', 'Dinner'

    class Meta:
        db_table = 'food'


