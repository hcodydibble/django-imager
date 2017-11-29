from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

# Create your models here.

PRIV = 'PRIVATE'
SHAR = 'SHARED'
PUB = 'PUBLIC'
PUBLISH_CHOICES = (
    (PRIV, 'Private'),
    (SHAR, 'Shared'),
    (PUB, 'Public')
)


class Photo(models.Model):
    image_file = ImageField(upload_to='django_imager/MEDIA')  # Will use Pillow once I figure it out.
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default=PRIV)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True)
    profile = models.ForeignKey(User, related_name='photo', on_delete=models.CASCADE, null=True)


class Album(models.Model):
    album_title = models.CharField(max_length=50, null=True)
    album_description = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True)
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default=PRIV)
    cover = ImageField(null=True)  # Same as Photo model.
    user = models.ForeignKey(User, related_name='album', on_delete=models.CASCADE, null=True)
    photo = models.ManyToManyField(Photo)
