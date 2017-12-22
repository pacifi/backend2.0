from django.contrib import admin
from .models import *


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
