from rest_framework import serializers
from .models import Rental, Plans, Subscriptions


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'customer', 'movie', 'rental_date', 'return_date']


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ['id', 'name', 'price', 'description', 'duration', 'features']


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['id', 'customer', 'plan',
                  'start_date', 'end_date', 'is_active']
