from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        style={'input_type': 'password'},
        min_length=8
    )

    class Meta:
        model = Customer
        fields = (
            'id',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'password',
        )

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        return get_user_model().objects.update_user(instance, **validated_data)

