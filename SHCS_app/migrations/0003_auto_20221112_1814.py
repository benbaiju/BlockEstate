# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-11-12 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0002_auto_20221112_1814'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
