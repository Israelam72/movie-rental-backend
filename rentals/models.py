from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# Create your models here.


class Rental(models.Model):
    """Represents a rental of a movie by a customer."""
    customer: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.PROTECT)
    movie: models.ForeignKey = models.ForeignKey(
        Movie, on_delete=models.PROTECT)
    rental_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    return_date: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def is_available(self) -> bool:
        return not Rental.objects.filter(movie=self, return_date__isnull=True).exists()
