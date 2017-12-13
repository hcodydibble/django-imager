from django import forms
from .models import Photo, Album


class NewPhotoForm(forms.ModelForm):
    """docstring for NewPhotoForm."""

    class Meta:
        """."""

        model = Photo
        exclude = []


class NewAlbumForm(forms.ModelForm):
    """docstring for NewAlbumForm."""

    class Meta:
        """."""

        model = Album
        exclude = ['user']


class UpdateAlbum(forms.ModelForm):
    """docstring for UpdateAlbum."""

    class Meta:
        """."""

        model = Album
        exclude = ['user']


class UpdatePhoto(forms.ModelForm):
    """docstring for UpdatePhoto."""

    class Meta:
        """."""

        model = Photo
        exclude = []
