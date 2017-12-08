"""."""
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from .forms import UpdateProfile, UpdateUser
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

    model = User
    # second_model = User
    template_name = 'django_imager/edit_profile.html'
    form_class = UpdateUser
    second_form_class = UpdateProfile
    success_url = '/profile/'
    #
    # def get_context_data(self, **kwargs):
    #     """."""
    #     context = super(ProfileEditView, self).get_context_data(**kwargs)
    #     if 'user_form' not in context:
    #         context['user_form'] = self.form_class(self.request.GET)
    #     if 'profile_form' not in context:
    #         context['profile_form'] = self.second_form_class(self.request.GET)
    #     return context

    # def get(self, request, *args, **kwargs):
    #     """."""
    #     super(ProfileEditView, self).get(request, *args, **kwargs)
    #     user_form = self.form_class
    #     profile_form = self.second_form_class
    #     return self.render_to_response(self.get_context_data(object=self.object, user_form=user_form, profile_form=profile_form))

    def get_object(self, queryset=None):  # pragma no cover
        """."""
        user = User.objects.get(id=self.kwargs['pk'])
        profile = ImagerProfile.objects.get(id=self.kwargs['pk'])
        return user
    #
    # def form_valid(self, form):  # pragma no cover
    #     """."""
    #     return super(ProfileEditView, self).form_valid(form)
