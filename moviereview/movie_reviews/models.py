from django.db import models

class MovieReview(models.Model):
    movie_name = models.CharField(max_length=200)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    review_text = models.TextField()

    def __str__(self):
        return self.movie_name

# Create your models here.
