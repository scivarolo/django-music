from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    num_of_members = models.IntegerField('Number of Members', default=1)

    def get_groups(self):
        return self.num_of_members > 1

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_year = models.IntegerField('Release Year')

    def __str__(self):
        return f"{self.title} by {self.artist.name}, {self.release_year}"


class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

