"""Images URLS."""

from django.conf.urls import url
from imager_images.views import (LibraryView,
                                 AlbumView,
                                 PhotoView,
                                 AlbumFormView,
                                 PhotoFormView,
                                 PublicPhotos,
                                 PublicAlbums,
                                 AlbumEditView,
                                 PhotoEditView)

urlpatterns = [
    url(r'library', LibraryView.as_view(), name='library'),
    url(r'library/(?P<user_search>[a-zA-Z0-9_.-]+$)', LibraryView.as_view()),
    url(r'^album/(?P<pk>\d+)', AlbumView.as_view(), name='album'),
    url(r'^albums/(?P<pk>\d+)/edit', AlbumEditView.as_view(), name='album_edit'),

    url(r'^photo/(?P<pk>\d+)', PhotoView.as_view(), name='photo'),
    url(r'^photos/(?P<pk>\d+)/edit', PhotoEditView.as_view(), name='photo_edit'),

    url(r'^album/add$', AlbumFormView.as_view(), name='new_album'),
    url(r'^photo/add$', PhotoFormView.as_view(), name='new_photo'),
    url(r'photos', PublicPhotos.as_view(), name='public_photos'),
    url(r'albums', PublicAlbums.as_view(), name='public_albums'),
]
