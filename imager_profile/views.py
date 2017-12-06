"""."""
from django.shortcuts import render
from django.contrib.auth.models import User


def profile_view(request, user_search=None):
    """The profile view."""
    if user_search:
        username = user_search
    else:  # pragma no cover
        username = request.user.username
    user = User.objects.get(username=username)
    profile = user.profile
    private_album_count = profile.user.album.filter(published='PRIVATE').count()
    private_photo_count = profile.user.photo.filter(published='PRIVATE').count()
    public_album_count = profile.user.album.filter(published='PUBLIC').count()
    public_photo_count = profile.user.photo.filter(published='PUBLIC').count()
    return render(request, 'django_imager/profile.html', {'profile': profile,
                                                          'ppho': private_photo_count,
                                                          'palb': private_album_count,
                                                          'pubpho': public_photo_count,
                                                          'pubalb': public_album_count})
