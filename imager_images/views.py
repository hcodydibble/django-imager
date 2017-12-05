"""Library view."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView

class LibraryView(ListView):
    """The library view."""

    template_name = 'django_imager/library.html'
    model = Album
    exclude = []

    def get_queryset(self):
        qs = super(LibraryView, self).get_queryset()
        qs = qs.filter(user__username=self.request.user)
        return qs



class AlbumView(ListView):
    """docstring for AlbumView."""

    template_name = 'django_imager/album.html'
    model = Album
    exclude = []

    def get_context_data(self, **kwargs):
        queryset = Album.objects.filter(id=self.kwargs['pk'])
        album = queryset.get()
        photos = album.photo_set.all()
        return {'photos': photos}
        



class PhotoView(DetailView):
    """docstring for PhotoView."""

    template_name = 'django_imager/photo.html'
    model = Photo
    exclude = []


class PublicPhotos(ListView):
    template_name = 'django_imager/public_photo.html'
    model = Photo

    def get_queryset(self):
        qs = super(PublicPhotos, self).get_queryset()
        qs = qs.filter(published='PUBLIC')
        return qs


class PublicAlbums(ListView):
    template_name = 'django_imager/public_album.html'
    model = Album

    def get_queryset(self):
        qs = super(PublicAlbums, self).get_queryset()
        qs = qs.filter(published='PUBLIC')
        return qs
