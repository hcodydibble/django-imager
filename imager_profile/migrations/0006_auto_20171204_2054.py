# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 20:54
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0005_auto_20171204_1905'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='imagerprofile',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]