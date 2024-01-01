from django.db import models
from .tag import Tag
from .artwork import Artwork

class ArtworkTag(models.Model):

    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
