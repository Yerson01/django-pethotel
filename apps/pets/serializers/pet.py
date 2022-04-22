from rest_framework.serializers import ModelSerializer

from apps.pets.models import Pet
from apps.customers.serializers import CustomerSerializer


class PetSerializer(ModelSerializer):
    owner = CustomerSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = ('name', 'type', 'size', 'owner')


