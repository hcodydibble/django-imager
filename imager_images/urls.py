"""Images URLS."""

from django.conf.urls import url
from imager_profile.views import profile_view
from imager_images.views import LibraryView, AlbumView, PhotoView

urlpatterns = [
    url(r'library', LibraryView.as_view()),
    url(r'^albums/(?P<pk>\d+)', AlbumView.as_view()),
    url(r'^photos/(?P<pk>\d+)', PhotoView.as_view()),
]
