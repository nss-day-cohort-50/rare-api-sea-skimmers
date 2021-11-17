from django.db import models
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey

class Comment(models.Model):
    """Comment model"""
    post = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now=True)
