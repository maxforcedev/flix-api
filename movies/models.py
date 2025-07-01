from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):

    title = models.CharField(max_length=200)
    year = models.DateField(blank=True, null=True,)
    description = models.TextField(blank=True, null=True)

    genres = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT,
        related_name= 'movies'
    )

    actors = models.ManyToManyField(
        Actor, 
        related_name= 'movies'
    )

    def __str__(self):
        return self.title
