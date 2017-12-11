"""Profile url."""

from django.conf.urls import url
from .views import AltProfileView, ProfileView, ProfileEditView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^edit/$', ProfileEditView.as_view(), name='profile_edit'),
    url(r'^(?P<user_search>[a-zA-Z0-9_.-]+$)', AltProfileView.as_view()),
]
