"""Library view."""

from imager_images.models import Album, Photo
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from .forms import NewPhotoForm


class AlbumFormView(CreateView):
    """docstring for AlbumForm."""

    model = Album
    template_name = 'django_imager/new_album.html'
    fields = ['title', 'description', 'cover', 'published']
    success_url = 'library'

    def post(self, request, *args, **kwargs):  # pragma: no cover
        """."""
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PhotoFormView(CreateView):
    """docstring for AlbumForm."""
    model = Photo
    template_name = 'django_imager/new_photo.html'
    fields = ['title', 'description', 'image_file', 'published', 'album']
    from_class = NewPhotoForm
    success_url = 'library'

    def post(self, request, *args, **kwargs):  # pragma: no cover
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

    def get_queryset(self):  # pragma no cover
        """."""
        qs = super(LibraryView, self).get_queryset()
        qs = qs.filter(user__username=self.kwargs.user)
        return qs


class AlbumView(ListView):
    """docstring for AlbumView."""

    template_name = 'django_imager/album.html'
    model = Album
    exclude = []

    def get_context_data(self, **kwargs):  # pragma no cover
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
    

class PublicPhotos(ListView):
    """."""

    template_name = 'django_imager/public_photo.html'
    model = Photo

    def get_queryset(self):
        """."""
        qs = super(PublicPhotos, self).get_queryset()
        qs = qs.filter(published='PUBLIC')
        return qs


class PublicAlbums(ListView):
    """."""

    template_name = 'django_imager/public_album.html'
    model = Album

    def get_queryset(self):
        """."""
        qs = super(PublicAlbums, self).get_queryset()
        qs = qs.filter(published='PUBLIC')
        return qs
