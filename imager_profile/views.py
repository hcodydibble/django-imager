from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def profile_view(request, user_search=None):
    """The profile view."""
    if user_search:
        username = user_search
    else:
        username = request.user.username
    user = User.objects.get(username=username)
    profile = user.profile
    photos = []
    albums = profile.user.album.all()
    for item in albums:
        for photo in item.photo.all():
            photos.append(photo)
    photo_count = len(photos)
    return render(request, 'django_imager/profile.html', {'profile': profile, 'count': photo_count})
