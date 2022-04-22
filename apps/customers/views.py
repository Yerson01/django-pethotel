from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.customers.serializers import CustomerSerializer


class CreateCustomerView(generics.CreateAPIView):
    """Register a new user in system"""
    serializer_class = CustomerSerializer


create_customer = CreateCustomerView.as_view()


class ManageCustomerView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """Manage account of authenticated user"""
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


manage_customer = ManageCustomerView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})
