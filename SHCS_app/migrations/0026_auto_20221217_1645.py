# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-17 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHCS_app', '0025_selling_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selling',
            name='Prop_id',
            field=models.CharField(max_length=255),
        ),
    ]
