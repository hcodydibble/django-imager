from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    image_file = models.ImageField()  # Will use Pillow once I figure it out.
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default=PRIV)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Album(models.Model):
    album_tile = models.CharField(max_length=50, null=True)
    album_description = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField()
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default=PRIV)
    cover = models.ImageField(null=True)  # Same as Photo model.
    user = models.OneToOneField(User, related_name='album', null=True)
    photo = models.ManyToManyField(Photo)
