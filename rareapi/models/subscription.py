from django.db import models

class Subscription(models.Model):
    """Subscription model"""
    created_on = models.DateField()
    follower = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="following")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    ended_on = models.DateField()