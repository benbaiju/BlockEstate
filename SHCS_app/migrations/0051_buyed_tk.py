# Generated by Django 4.1.5 on 2023-02-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SHCS_app", "0050_remove_token_preowner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buyed_tk",
            fields=[
                ("r_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("p_id", models.CharField(max_length=255)),
                ("tk_name", models.CharField(max_length=255)),
                ("hash1", models.CharField(max_length=255)),
                ("p_type", models.CharField(max_length=255)),
                ("im", models.CharField(max_length=255)),
                ("details", models.CharField(max_length=255)),
                ("amnt", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
            ],
        ),
    ]
