# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-02-16 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0037_buyed_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='selling',
            name='hash1',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
