from django.db import models
from time import localtime as lt

year = []
for i in range(1992, lt().tm_year+1):
    year.append((i, str(i)))

tuple(year)

class Director(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(blank=False, null=False, default='New Album', max_length=150)
    director = models.ForeignKey(Director, related_name='director_name', on_delete=models.CASCADE)
    year = models.IntegerField(choices=year)
    time_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    movie = models.ForeignKey(Album, related_name="Movie", on_delete=models.CASCADE)
    song = models.FileField(upload_to='.music/songs/')
    def __str__(self):

        # .music/songs/iSongs.info_03_-_Neekem_Kaavaalo_Cheppu.mp3
        song = str(self.song).split('/')[2]
        return song

