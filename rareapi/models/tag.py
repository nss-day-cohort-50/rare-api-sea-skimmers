from django.db import models

class Tag(models.Model):
    """Tag model"""
    label = models.CharField(max_length=50)