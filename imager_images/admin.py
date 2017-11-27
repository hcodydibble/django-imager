from django.contrib import admin

# Register your models here.
from imager_profile.models import ImagerProfile


@admin.register(ImagerProfile)
class ImagerProfileAdmin(admin.ModelAdmin):
    pass
