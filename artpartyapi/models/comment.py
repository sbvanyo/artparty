from django.db import models
from .user import User
from .artwork import Artwork

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created_on = models.DateTimeField()
