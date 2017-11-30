"""."""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """Class for the profile view."""
    model = User
    template_name = 'django_imager/profile.html'
    
    def get_context_data(self, **kwargs):
        if kwargs:
            username = kwargs['user_search']
        else:
            username = self.request.user.username
        user = User.objects.get(username=username)
        profile = user.profile
        photos = []
        albums = profile.user.album.all()
        for item in albums:
            for photo in item.photo_set.all():
                photos.append(photo)
        photo_count = len(photos)
        return {'profile': profile, 'count': photo_count}
