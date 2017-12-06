from django import forms
from .models import Photo, Album


class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = []


class NewAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []
