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

    # def get_context_data(self, pk):
    #     super(AlbumView, self).get_context_data()
    #     user = User.objects.get(username='hcodydibble')
    #     album = user.album.get(id=2)
    #     image = album.photo_set.get(id=pk)
    #     return {'image': image}



class PhotoView(DetailView):
    """docstring for PhotoView."""

    template_name = 'django_imager/photo.html'
    model = Photo
    exclude = []
