# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-17 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0024_auto_20221217_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='selling',
            name='amount',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]