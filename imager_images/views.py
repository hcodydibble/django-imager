"""Library view."""

from imager_images.models import Album, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import NewPhotoForm, UpdateAlbum, UpdatePhoto
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class AlbumFormView(LoginRequiredMixin, CreateView):
    """docstring for AlbumForm."""

    model = Album
    template_name = 'django_imager/new_album.html'
    fields = ['title', 'description', 'cover', 'published']
    success_url = 'library'

    def post(self, request, *args, **kwargs):  # pragma: no cover
        """."""
        form = self.get_form()
        if form.is_valid():
            form = form.save()
            form.user = User.objects.get(username=request.user.username)
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)


class AlbumEditView(LoginRequiredMixin, UpdateView):
    """docstring for AlbumEditView."""

    model = Album
    template_name = 'django_imager/edit_album.html'
    form_class = UpdateAlbum
    success_url = 'library'

    def get_object(self, **kwargs):  # pragma no cover
        """."""
        album = Album.objects.get(id=self.kwargs['pk'])
        return album

    def form_valid(self, form):  # pragma no cover
        """."""
        return super(AlbumEditView, self).form_valid(form)


class PhotoFormView(LoginRequiredMixin, CreateView):
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
            form = form.save()
            form.profile = User.objects.get(username=request.user.username)
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)


class PhotoEditView(LoginRequiredMixin, UpdateView):
    """docstring for PhotoEditView."""

    model = Photo
    template_name = 'django_imager/edit_photo.html'
    form_class = UpdatePhoto
    success_url = 'library'

    def get_object(self, queryset=None):  # pragma no cover
        """."""
        album = Photo.objects.get(id=self.kwargs['pk'])
        return album

    def form_valid(self, form):  # pragma no cover
        """."""
        return super(PhotoEditView, self).form_valid(form)


class LibraryView(LoginRequiredMixin, ListView):
    """The library view."""

    template_name = 'django_imager/library.html'
    model = Album
    exclude = []

    def get_context_data(self, **kwargs):  # pragma no cover
        """Provide context for the view."""
        context = super(LibraryView, self).get_context_data(**kwargs)
        request = context['view'].request

        album_list = Album.objects.filter(user=self.request.user.id)
        album_list.order_by('id')
        album_paginator = Paginator(album_list, 4)
        if 'album_page' in request.GET:
            album_page = request.GET.get('album_page').split('?photo_page=')[0]
        else:
            album_page = 1
        try:
            context['albums'] = album_paginator.page(album_page)
        except PageNotAnInteger:
            context['albums'] = album_paginator.page(1)
        except EmptyPage:
            context['albums'] = album_paginator.page(album_paginator.num_pages)
        return context


class AlbumView(ListView):
    """docstring for AlbumView."""

    template_name = 'django_imager/album.html'
    model = Album
    exclude = []

    def get_context_data(self, **kwargs):  # pragma no cover
        """."""
        context = super(AlbumView, self).get_context_data(**kwargs)
        request = context['view'].request
        queryset = Album.objects.filter(id=self.kwargs['pk'])
        album = queryset.get()
        context['album'] = album
        photo_list = album.photo_set.all()
        photo_list.order_by('id')
        photo_paginator = Paginator(photo_list, 4)
        if 'photo_page' in request.GET:
            photo_page = request.GET.get('photo_page').split('?photo_page=')[0]
        else:
            photo_page = 1
        context['photos'] = photo_paginator.page(photo_paginator.num_pages)
        try:
            context['photos'] = photo_paginator.page(photo_page)
        except PageNotAnInteger:
            context['photos'] = photo_paginator.page(1)
        except EmptyPage:
            context['photos'] = photo_paginator.page(photo_paginator.num_pages)
        return context


class PhotoView(DetailView):
    """docstring for PhotoView."""

    template_name = 'django_imager/photo.html'
    model = Photo
    exclude = []


class PublicPhotos(ListView):
    """."""

    template_name = 'django_imager/public_photo.html'
    model = Photo

    def get_context_data(self, **kwargs):  # pragma no cover
        """Provide context for the view."""
        context = super(PublicPhotos, self).get_context_data(**kwargs)
        request = context['view'].request
        photo_list = Photo.objects.all()
        photo_list.order_by('id')
        photo_paginator = Paginator(photo_list, 4)
        if 'photo_page' in request.GET:
            photo_page = request.GET.get('photo_page').split('?photo_page=')[0]
        else:
            photo_page = 1
        context['photos'] = photo_paginator.page(photo_paginator.num_pages)
        try:
            context['photos'] = photo_paginator.page(photo_page)
        except PageNotAnInteger:
            context['photos'] = photo_paginator.page(1)
        except EmptyPage:
            context['photos'] = photo_paginator.page(photo_paginator.num_pages)
        return context


class PublicAlbums(ListView):
    """."""

    template_name = 'django_imager/public_album.html'
    model = Album

    def get_context_data(self, **kwargs):  # pragma no cover
        """Provide context for the view."""
        context = super(PublicAlbums, self).get_context_data(**kwargs)
        request = context['view'].request
        album_list = Album.objects.all()
        album_list.order_by('id')
        photo_paginator = Paginator([], 4)
        album_paginator = Paginator(album_list, 4)
        if 'album_page' in request.GET:
            album_page = request.GET.get('album_page').split('?photo_page=')[0]
        else:
            album_page = 1
        context['photos'] = photo_paginator.page(photo_paginator.num_pages)
        try:
            context['albums'] = album_paginator.page(album_page)
        except PageNotAnInteger:
            context['albums'] = album_paginator.page(1)
        except EmptyPage:
            context['albums'] = album_paginator.page(album_paginator.num_pages)
        return context
