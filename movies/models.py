from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    """Represents a movie in the rental system with its details."""
    title: models.CharField = models.CharField(max_length=200)
    genre: models.CharField = models.CharField(max_length=200)
    director: models.CharField = models.CharField(max_length=200)
    release_year: models.IntegerField = models.IntegerField()
    synopsis: models.TextField = models.TextField()
    rating: models.FloatField = models.FloatField()

    def is_available(self) -> bool:
        return not Rental.objects.filter(movie=self, return_date__isnull=True).exists()


class Rental(models.Model):
    """Represents a rental of a movie by a customer."""
    customer: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.PROTECT)
    movie: models.ForeignKey = models.ForeignKey(
        Movie, on_delete=models.PROTECT)
    rental_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    return_date: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
