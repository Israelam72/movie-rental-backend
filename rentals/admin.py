from django.contrib import admin
from .models import Rental
# Register your models here.


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'movie', 'rental_date', 'return_date')
    list_filter = ('customer', 'movie')
    search_fields = ('customer__username', 'movie__title')
    date_hierarchy = 'rental_date'
