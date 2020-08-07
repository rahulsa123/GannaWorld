from django.contrib import admin

# Register your models here.
from .models import Song, PlayList

from .forms import SongAdminForm


class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = SongAdminForm


class PlayListAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Song, SongAdmin)
admin.site.register(PlayList, PlayListAdmin)
