from django.db import models

# Create your models here.


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)


class Tags(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)


class Video(models.Model):
    upload = models.FileField()
    title = models.CharField(max_length=50)
    views = models.IntegerField()
    description = models.CharField(max_length=5000)
    date_uploaded = models.DateField(auto_now=True)
    likes = models.IntegerField()
    tags = models.ManyToManyField(Tags)
    category = models.ManyToManyField(Category)
    playlist = models.ForeignKey(Playlist, related_name="videos")



