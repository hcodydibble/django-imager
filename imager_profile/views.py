"""."""
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UpdateUserForm
from .models import ImagerProfile


class ProfileView(TemplateView):
    """Class for the profile view."""

    model = User
    template_name = 'django_imager/profile.html'

    def get_context_data(self):  # pragma: no cover
        username = self.request.user.username
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


class AltProfileView(TemplateView):
    """Class view for profiles that aren't the logged in user."""

    model = User
    template_name = 'django_imager/profile.html'

    def get_context_data(self, **kwargs):
        username = kwargs['user_search']
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
    success_url = reverse_lazy('profile')
    form_class = UpdateUserForm

    def get_object(self):
        """Overwrite UpdateView to get logged in users profile."""
        return self.request.user.profile

    def form_valid(self, form):  # pragma: no cover
        """Check that form is valid before editing."""
        self.object = form.save()
        self.object.user.username = form.cleaned_data['Username']
        self.object.user.email = form.cleaned_data['Email']
        self.object.user.first_name = form.cleaned_data['First name']
        self.object.user.last_name = form.cleaned_data['Last name']
        self.object.user.save()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
