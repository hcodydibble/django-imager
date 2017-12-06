"""Views for the Django Imager Site."""
import random
from django.views.generic import TemplateView
from imager_images.models import Photo


class HomeView(TemplateView):
    """Class for the home view."""
    template_name = 'django_imager/homepage.html'

    def get_context_data(self):
        super(HomeView, self).get_context_data()
        list_images = Photo.objects.filter(published='PUBLIC')
        choice = random.choice(list_images)
        return {'choice': choice}
