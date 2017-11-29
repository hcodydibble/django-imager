"""Library view."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView


class LibraryView(ListView):
    """The library view."""

    template_name = 'django_imager/library.html'
    model = Album
    exclude = []


class AlbumView(ListView):
    """docstring for AlbumView."""

    template_name = 'django_imager/album.html'
    model = Album
    exclude = []


class PhotoView(DetailView):
    """docstring for PhotoView."""

    template_name = 'django_imager/photo.html'
    model = Photo
    exclude = []
