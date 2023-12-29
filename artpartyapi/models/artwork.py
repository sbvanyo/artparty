from django.db import models
from .user import User
from .artist import Artist
from .collection import Collection

class Artwork(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    medium = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_created = models.DateField()
    age_created = models.IntegerField()
