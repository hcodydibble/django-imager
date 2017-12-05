"""Images URLS."""

from django.conf.urls import url
from imager_images.views import LibraryView, AlbumView, PhotoView, AlbumFormView, PhotoFormView

urlpatterns = [
    url(r'library', LibraryView.as_view(), name='library'),
    url(r'library/(?P<user_search>[a-zA-Z0-9_.-]+$)', LibraryView.as_view()),
    url(r'^album/(?P<pk>\d+)', AlbumView.as_view(), name='album'),
    url(r'^photo/(?P<pk>\d+)', PhotoView.as_view(), name='photo'),
    url(r'^album/add$', AlbumFormView.as_view(), name='new_album'),
    url(r'^photo/add$', PhotoFormView.as_view(), name='new_photo'),
]
