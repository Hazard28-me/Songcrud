from email.policy import default
from tkinter import CASCADE
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

class Song(models.Model):
    title = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

class Lyric(models.Model):
    content = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.IntegerField()