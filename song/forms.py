from django import forms
from .models import Song, PlayList


class SongAdminForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "owner", "song_file",
                  "cover_image", "user_likes", "slug"]
        widgets = {
            "song_file": forms.FileInput(attrs={'accept': 'audio/*'})
        }


class SongCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "song_file",
                  "cover_image"]
        widgets = {
            "song_file": forms.FileInput(attrs={'accept': 'audio/*'})
        }


class PlayListCreateForm (forms.ModelForm):
    class Meta:
        model = PlayList
        fields = ["title", "songs",
                  "cover_image"]
        widgets = {
            "songs": forms.SelectMultiple
        }
