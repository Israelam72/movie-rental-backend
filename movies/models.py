from django.db import models


class Movie(models.Model):
    """Represents a movie in the rental system with its details."""
    title: models.CharField = models.CharField(max_length=200)
    genre: models.CharField = models.CharField(max_length=200)
    director: models.CharField = models.CharField(max_length=200)
    release_year: models.IntegerField = models.IntegerField()
    synopsis: models.TextField = models.TextField()
    rating: models.FloatField = models.FloatField()
    image_url: models.URLField = models.URLField(
        max_length=200, null=True, blank=True)
