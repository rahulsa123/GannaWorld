from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from PIL import Image


class Profile(models.Model):
    image = models.ImageField(
        upload_to="user/profile/", default="default.png")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f'{self.user.username} profile'

    def get_absolute_url(self):
        return reverse("user:profile")

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
