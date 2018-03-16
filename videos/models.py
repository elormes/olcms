from django.db import models

# Create your models here.


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


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
    views = models.IntegerField()
    description = models.CharField(max_length=5000)
    date_uploaded = models.DateField(auto_now=True)
    likes = models.IntegerField()
    tags = models.ManyToManyField(Tags)
    category = models.ManyToManyField(Category)
    playlist = models.ForeignKey(Playlist, related_name="videos")

    def __str__(self):
        return self.title



