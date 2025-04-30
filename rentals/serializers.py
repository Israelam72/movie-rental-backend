from rest_framework import serializers
from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'customer', 'movie', 'rental_date', 'return_date']
