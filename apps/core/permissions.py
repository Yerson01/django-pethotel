from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.core.utils import instance_attr_is_value


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        can_pass = request.method in SAFE_METHODS
        if not can_pass:
            lookup_attr = 'owner_lookup_field'
            message_params = (view.__class__.__name__, self.__class__.__name__, lookup_attr)
            assert hasattr(view, lookup_attr), '%s: %s needs `%s` attr' % message_params
            lookup = getattr(view, lookup_attr)
            is_owner = instance_attr_is_value(obj, lookup, request.user.id)
            can_pass = request.user.is_authenticated and is_owner
        return can_pass