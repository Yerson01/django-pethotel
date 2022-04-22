from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.core.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('date_joined',)
    list_display = ('id', 'first_name', 'last_name', 'email',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important Dates'), {
            'fields': ('date_joined', 'last_login')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                ('first_name', 'last_name'),
                ('email',),
                ('password1', 'password2')
            ),
        }),
    )

