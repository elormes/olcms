from django.db import models
import os

# Create your models here.


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.name)


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Video(models.Model):
    upload = models.FileField()
    title = models.CharField(max_length=50)
    views = models.IntegerField(default=0,blank=True)
    description = models.CharField(max_length=5000)
    date_uploaded = models.DateField(auto_now=True)
    likes = models.IntegerField(default=0, blank=True)
    tags = models.ManyToManyField(Tags)
    category = models.ManyToManyField(Category)
    playlist = models.ForeignKey(Playlist, related_name="videos", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.upload.name)



