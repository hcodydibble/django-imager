from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.test import TestCase

import factory

from django.test import Client

import pytest

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class ProfileTestCase(TestCase):
    pass
