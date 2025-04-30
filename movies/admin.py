from django.contrib import admin
from .models import Movie, Rental

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'release_year', 'rating')
    list_filter = ('genre', 'director')
    search_fields = ('title', 'director')
    list_per_page = 10


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'movie', 'rental_date', 'return_date')
    list_filter = ('customer', 'movie')
    search_fields = ('customer__username', 'movie__title')
    date_hierarchy = 'rental_date'
