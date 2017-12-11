"""Update user profile."""
from django import forms
from .models import ImagerProfile


class UpdateUserForm(forms.ModelForm):
    """docstring for UpdateUser."""

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['First name'] = forms.CharField(initial=self.instance.user.first_name)
        self.fields['Last name'] = forms.CharField(initial=self.instance.user.last_name)
        self.fields['Username'] = forms.CharField(initial=self.instance.user.username)
        self.fields['Email'] = forms.CharField(initial=self.instance.user.email)
        del self.fields['user']

    class Meta:

        model = ImagerProfile
        exclude = []
