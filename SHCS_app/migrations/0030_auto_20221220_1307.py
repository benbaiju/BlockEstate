# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-20 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0029_token_preowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='selling',
            name='username',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='username',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
