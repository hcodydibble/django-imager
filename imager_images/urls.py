"""Images URLS."""

from django.conf.urls import url
from imager_images.views import LibraryView, AlbumView, PhotoView

urlpatterns = [
    url(r'library', LibraryView.as_view(), name='library'),
    url(r'^albums/(?P<pk>\d+)', AlbumView.as_view(), name='album'),
    url(r'^photos/(?P<pk>\d+)', PhotoView.as_view(), name='photo'),
]
