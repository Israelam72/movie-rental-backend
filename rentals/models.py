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
    is_returned: models.BooleanField = models.BooleanField(default=False)

    def is_available(self) -> bool:
        return not Rental.objects.filter(movie=self, return_date__isnull=True).exists()


class Plans(models.Model):
    """Represents a plan for a customer"""
    name: models.CharField = models.CharField()
    price: models.FloatField = models.FloatField()
    description: models.TextField = models.TextField()
    duration: models.IntegerField = models.IntegerField()
    features: models.JSONField = models.JSONField(default=list)


class Subscriptions(models.Model):
    """Represents a subscription of a customer"""
    customer: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.PROTECT)
    plan: models.ForeignKey = models.ForeignKey(
        Plans, on_delete=models.PROTECT)
    start_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    end_date: models.DateTimeField = models.DateTimeField(
        null=True, blank=True)
    is_active: models.BooleanField = models.BooleanField(default=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.customer.username} - {self.plan.name} - {self.start_date} - {self.end_date}"

    def __repr__(self) -> str:
        return f"{self.customer.username} - {self.plan.name}"
