from django.db import models

# Create your models here.

class Collaborative_Music(models.Model):
    title = models.CharField(max_length=200)
    rating = models.BigIntegerField()
    user_id=models.BigIntegerField()
    song_id=models.BigIntegerField()

class Contentbase_Music(models.Model):
    artist_name = models.CharField(max_length=200)
    track_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    concat = models.CharField(max_length=200)