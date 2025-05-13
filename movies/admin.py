from django.contrib import admin
from .models import Movie
from rentals.models import Plans, Subscriptions

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'release_year', 'rating')
    list_filter = ('genre', 'director')
    search_fields = ('title', 'director')
    list_per_page = 10


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'duration', 'features')
    list_filter = ('name', 'price', 'duration')
    search_fields = ('name', 'description')
    list_per_page = 10


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'plan', 'start_date', 'end_date', 'is_active')
    list_filter = ('customer', 'plan', 'start_date', 'end_date', 'is_active')
    search_fields = ('customer', 'plan', 'start_date', 'end_date', 'is_active')
    list_per_page = 10
