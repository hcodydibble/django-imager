# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-27 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0007_auto_20171127_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='date_published',
            field=models.DateTimeField(null=True),
        ),
    ]
