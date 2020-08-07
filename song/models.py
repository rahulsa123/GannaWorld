from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class Song(models.Model):
    title = models.CharField(max_length=150)
    song_file = models.FileField(upload_to="song/file/")
    published = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to="song/cover/", default="default_cover.png")

    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="user_likes", blank=True)

    slug = models.CharField(max_length=250,
                            unique_for_date="published")

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return f"song {self.title} by {self.owner.username}"

    def save(self, *args, **kwargs):
        super(Song, self).save(*args, **kwargs)
        img = Image.open(self.cover_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover_image.path)

    def get_absolute_url(self):
        return reverse("song:song_detail", args=[
            self.pk,
            self.published.year,
            self.published.month,
            self.published.day,
            self.slug
        ])


class PlayList(models.Model):
    title = models.CharField(max_length=150)
    songs = models.ManyToManyField(Song, related_name="songs")
    cover_image = models.ImageField(
        upload_to="playlist/cover/", default="default_cover.png")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=250,
                            unique_for_date="published")
    published = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.title} playlist by {self.owner.username}'

    def save(self, *args, **kwargs):
        super(PlayList, self).save(*args, **kwargs)
        img = Image.open(self.cover_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover_image.path)

    def get_absolute_url(self):
        return reverse("song:playlist_detail", args=[
            self.pk,
            self.published.year,
            self.published.month,
            self.published.day,
            self.slug
        ])
