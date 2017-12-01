"""Images URLS."""

from django.conf.urls import url
from imager_images.views import LibraryView, AlbumView, PhotoView, AlbumFormView

urlpatterns = [
    url(r'library', LibraryView.as_view(), name='library'),
    url(r'^album/(?P<pk>\d+)', AlbumView.as_view(), name='album'),
    url(r'^photo/(?P<pk>\d+)', PhotoView.as_view(), name='photo'),
    url(r'^new-album', AlbumFormView.as_view(), name='new_album'),
]
