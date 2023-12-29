from django.db import models
from .artist import Artist
from .artwork import Artwork
class ArtworkArtist(models.Model):

    artwork_id = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
