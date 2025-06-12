from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(unique=True)
    terms_accepted = models.BooleanField(default=False)
