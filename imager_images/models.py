from django.db import models
from django.utils import timezone
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


class Album(models.Model):
    """Album model."""

    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True)
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default=PRIV)
    cover = ImageField(upload_to='', null=True)
    user = models.ForeignKey(User, related_name='album', on_delete=models.CASCADE, null=True)

    def __str__(self):  # pragma no cover
        """."""
        return self.title


class Photo(models.Model):
    """.Photo model."""

    image_file = ImageField(upload_to='')
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default=PRIV)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True)
    profile = models.ForeignKey(User, related_name='photo', on_delete=models.CASCADE, null=True)
    album = models.ManyToManyField(Album)
