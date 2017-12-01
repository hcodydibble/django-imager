"""Library view."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django import forms


class AlbumFormView(CreateView):
    """docstring for AlbumForm."""

    model = Album
    template_name = 'django_imager/new_album.html'
    fields = ['title', 'description', 'cover', 'published']
    success_url = 'library'

    def post(self, request, *args, **kwargs):
        """."""
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


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
