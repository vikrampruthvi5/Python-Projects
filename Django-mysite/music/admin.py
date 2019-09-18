from django.contrib import admin

'''
Two steps to be followed
1. Import model
2. register to admin
'''

from .models import Album, Director, Song


#admin.site.register(Album)
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name','director', 'year')
    list_filter = ('director',)
    #list_editable = ('year',)
    list_per_page = 10


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Song)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('movie', 'song')