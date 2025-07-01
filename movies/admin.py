from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):

    list_display = ('title', 'release_date', 'genres')
