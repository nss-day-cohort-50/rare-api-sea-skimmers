from django.db import models
from django.db.models.fields import CharField

class Reaction(models.Model):
    """Reaction model"""
    label = models.CharField(max_length=50)
    image_url = models.ImageField()