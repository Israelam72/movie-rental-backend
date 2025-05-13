from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
    path('plans/', views.get_plans, name='get-plans'),
]
