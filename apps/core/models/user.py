import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.managers import UserManager


def default_username():
    return 'user%s' % uuid.uuid4().hex[:8]


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    username = models.CharField(max_length=150, unique=True, default=default_username)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'
