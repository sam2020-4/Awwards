# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-26 15:56
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]