from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('all/', views.get_movies, name='get-movies'),
]
