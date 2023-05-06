from django.db import models

class Book (models.Model):
    list_count = models.IntegerField()
    text = models.TextField()
