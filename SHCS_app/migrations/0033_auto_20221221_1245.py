# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0032_token_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='Button',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='Cuholder',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
