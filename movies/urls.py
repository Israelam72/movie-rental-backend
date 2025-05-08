from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.get_movies, name='get-movies'),
    path('home/', views.get_home_movies, name='get-home-movies'),
]
