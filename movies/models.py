from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    """Represents a movie in the rental system with its details."""
    title: models.CharField = models.CharField(max_length=200)
    genre: models.CharField = models.CharField(max_length=200)
    director: models.CharField = models.CharField(max_length=200)
    release_year: models.IntegerField = models.IntegerField()
    synopsis: models.TextField = models.TextField()
    rating: models.FloatField = models.FloatField()
