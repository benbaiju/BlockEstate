# Generated by Django 4.1.5 on 2023-02-25 03:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("SHCS_app", "0043_buyed_im_buyed_p_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="buyed",
            name="details",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="buyed",
            name="phone",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
