"""Images URLS."""

from django.conf.urls import url
from imager_profile.views import profile_view
from imager_images.views import LibraryView, AlbumView, PhotoView, PublicPhotos, PublicAlbums

urlpatterns = [
    url(r'library', LibraryView.as_view(), name='library'),
    url(r'^albums/(?P<pk>\d+)', AlbumView.as_view(), name='album'),
    url(r'^photos/(?P<pk>\d+)', PhotoView.as_view(), name='photo'),
    url(r'photos', PublicPhotos.as_view(), name='public_photos'),
    url(r'albums', PublicAlbums.as_view(), name='public_albums'),
]
