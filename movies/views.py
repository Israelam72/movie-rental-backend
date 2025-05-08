from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer

from .models import Movie

# Create your views here.


@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_home_movies(request):
    movies = Movie.objects.all()[:4]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
