"""Library view."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


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

    def get_context_data(self, **kwargs):
        """."""
        queryset = Album.objects.filter(id=self.kwargs['pk'])
        album = queryset.get()
        photos = album.photo_set.all()
        return {'photos': photos, 'album': album}


class PhotoView(DetailView):
    """docstring for PhotoView."""

    template_name = 'django_imager/photo.html'
    model = Photo
    exclude = []
