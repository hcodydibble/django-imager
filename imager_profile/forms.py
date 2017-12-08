"""Update user profile."""
from django import forms
from .models import ImagerProfile
from django.contrib.auth.models import User


class UpdateProfile(forms.ModelForm):
    """docstring for UpdateProfile."""

    class Meta:
        """."""

        model = ImagerProfile
        exclude = []


class UpdateUser(forms.ModelForm):
    """docstring for UpdateUser."""

    class Meta:
        """."""

        model = User
        exclude = []
