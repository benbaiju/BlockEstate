# Generated by Django 4.1.5 on 2023-03-02 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("SHCS_app", "0053_sellingg_tokenn_delete_selling_delete_token"),
    ]

    operations = [
        migrations.RenameModel(old_name="Sellingg", new_name="Selling",),
        migrations.RenameModel(old_name="Tokenn", new_name="Token",),
    ]
