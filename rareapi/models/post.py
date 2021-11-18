from django.db import models
from rareapi.models import Comment

class Post(models.Model):
    """Post model"""
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.URLField()
    content = models.TextField()
    approved = models.BooleanField()
    

    @property
    def isApproved(self):
        """Average rating calculated attribute for each game"""
        ratings = GameRating.objects.filter(game_id=self.id)
        # Sum all of the ratings for the game
        total_rating = 0
        if ratings:
            for rating in ratings:
                total_rating += rating.rating
            average = total_rating / len(ratings)
        else:
            average = 0
            

        return average