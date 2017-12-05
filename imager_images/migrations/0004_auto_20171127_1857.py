# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-27 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_auto_20171125_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(),
        ),
        migrations.RemoveField(
            model_name='album',
            name='photo',
        ),
        migrations.AddField(
            model_name='album',
            name='photo',
            field=models.ManyToManyField(to='imager_images.Photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_published',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
