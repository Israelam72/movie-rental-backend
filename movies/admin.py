from django.contrib import admin
from .models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'release_year', 'rating')
    list_filter = ('genre', 'director')
    search_fields = ('title', 'director')
    list_per_page = 10
