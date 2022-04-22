from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models.timestamp import TimestampMixin


class User(AbstractUser, TimestampMixin):
  phone_number = models.CharField(max_length=15)

  class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'
    default_related_name = 'users'
