from django.apps import AppConfig


class PetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pets'
    label = 'pets'
    verbose_name = 'Pet'
    verbose_name_plural = 'Pets'
