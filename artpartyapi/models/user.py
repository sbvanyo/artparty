from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    prof_pic = models.CharField(max_length=100)
    created_on = models.DateField()
    uid = models.CharField(max_length=50)
