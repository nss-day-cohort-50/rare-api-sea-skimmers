from django.db import models

class Post(models.Model):
    """Post model"""
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.ImageField()
    content = models.TextField()
    approved = models.BooleanField()