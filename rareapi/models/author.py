from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    """Author model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image_url = models.ImageField()
    created_on = models.DateTimeField()
    active = models.BooleanField()