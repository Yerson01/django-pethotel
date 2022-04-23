from django.contrib.auth.models import BaseUserManager

from apps.core.utils import clean_word


class UserManager(BaseUserManager):
    """
    This user manager uses email field instead of 
    username as primary field
    """

    def create(self, **kwargs):
        kwargs = self._prepare_fields(kwargs)
        return super(UserManager, self).create(**kwargs)

    def _prepare_fields(self, fields: dict):
        first_name = clean_word(fields.get('first_name', ''))
        last_name = clean_word(fields.get('last_name', ''))
        fields.update(first_name=first_name, last_name=last_name)
        return fields

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a new user with the given email and password.
        """
        extra_fields = self._prepare_fields(extra_fields)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.update(dict(is_staff=True))
        extra_fields.update(dict(is_superuser=True))
        return self._create_user(email, password, **extra_fields)

    def update_user(self, instance, **kwargs):
        password = kwargs.pop('password', None)
        kwargs = self._prepare_fields(kwargs)

        for attr, value in kwargs.items():
            if value:
                setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
