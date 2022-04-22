from django.apps import AppConfig


class LodgingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.lodging'
    label = 'lodging'
    verbose_name = 'Lodging'
    verbose_name_plural = 'Lodgings'
