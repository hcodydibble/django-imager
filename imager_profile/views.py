"""."""
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from .forms import UpdateProfile
from .models import ImagerProfile


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


class ProfileEditView(UpdateView):
    """docstring for ProfileEditView."""

    model = ImagerProfile
    template_name = 'django_imager/edit_profile.html'
    form_class = UpdateProfile
    success_url = '/profile/'

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileEditView, self).get_context_data(**kwargs)
    #     context['second_model'] = User.objects.get(id=self.kwargs['pk'])
    #     return context

    def get_object(self, queryset=None):  # pragma no cover
        """."""
        user = User.objects.get(id=self.kwargs['pk'])
        profile = ImagerProfile.objects.get(id=self.kwargs['pk'])
        return profile

    def form_valid(self, form):  # pragma no cover
        """."""
        return super(ProfileEditView, self).form_valid(form)
