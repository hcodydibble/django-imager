"""Library view."""

from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def library_view(request, user_search=None):
    """The library view."""
    if user_search:
        username = user_search
    else:
        username = request.user.username
    user = User.objects.get(username=username)
    profile = user.profile
    albums = []
    for album in profile.user.album.all():
        albums.append(album)
    return render(request, 'django_imager/library.html', {'album': albums})
