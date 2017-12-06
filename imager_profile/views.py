"""."""
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
            username = self.request.user.username  # pragma: no cover
        user = User.objects.get(username=username)
        profile = user.profile
        public_album_count = profile.user.album.filter(published='PUBLIC').count()
        public_photo_count = profile.user.photo.filter(published='PUBLIC').count()
        private_album_count = profile.user.album.filter(published='PRIVATE').count()
        private_photo_count = profile.user.photo.filter(published='PRIVATE').count()
        return {'profile': profile,
                'pubpho': public_photo_count,
                'ppho': private_photo_count,
                'pubalb': public_album_count,
                'palb': private_album_count}
