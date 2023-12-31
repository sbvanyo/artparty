from django.db import models
from .artist import Artist
from .artwork import Artwork
class ArtworkArtist(models.Model):

    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
