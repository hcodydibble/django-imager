"""Views for the Django Imager Site."""
from django.shortcuts import render
from django.core.mail import send_mail


def home_view(request):
    """The home view."""
    return render(request, 'django_imager/base.html')


# def send_email(request):
#     """."""
#     subject = request.POST.get()
#     return render(request, 'registration/registration_complete.html')
