"""Update user profile."""
from django import forms
from django.contrib.auth.models import User
from .models import ImagerProfile
from betterforms.multiform import MultiModelForm



class UserEditForm(forms.ModelForm):

    class Meta:
        models = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = ImagerProfile
        exclude = []


class UpdateUser(MultiModelForm):
    """docstring for UpdateUser."""

    form_classes = {
        'user': UserEditForm,
        'profile': ProfileEditForm
    }
