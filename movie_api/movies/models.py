from django.db import models

# Create your models here.
class Movie(models.Model):
    # `movie_name`
    # `language`
    # `director`
    # `release_year`
    # `duration`
    # `rating`
    movie_name=models.CharField(max_length=50)
    language=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    release_year=models.IntegerField()
    duration=models.IntegerField()
    rating=models.IntegerField()
