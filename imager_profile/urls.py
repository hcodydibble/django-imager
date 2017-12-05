"""Profile url."""

from django.conf.urls import url
from imager_profile.views import ProfileView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^(?P<user_search>[a-zA-Z0-9_.-]+$)', ProfileView.as_view()),
]
