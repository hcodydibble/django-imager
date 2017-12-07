"""Profile url."""

from django.conf.urls import url
from imager_profile.views import ProfileView, ProfileEditView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^(?P<user_search>[a-zA-Z0-9_.-]+$)', ProfileView.as_view()),
    url(r'edit/(?P<pk>\d+)', ProfileEditView.as_view(), name='profile_edit'),
]
