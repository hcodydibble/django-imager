"""Views for the Django Imager Site."""
import random
import os
from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Class for the home view."""
    template_name = 'django_imager/homepage.html'


    def get_context_data(self):
        super(HomeView, self).get_context_data()
        list_images = os.listdir()
        choice = random.choice(list_images)
        return {'choice': choice}
