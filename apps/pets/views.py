from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.pets.models import Pet
from apps.pets.serializers import PetSerializer
from apps.core.permissions import IsOwnerOrReadOnly


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = PetSerializer

    filter_backends = (SearchFilter,)
    search_fields = ('name', 'owner__first_name', 'owner__last_name',)
    owner_lookup_field = 'owner_id'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
