# Generated by Django 4.1.3 on 2022-11-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SHCS_app", "0003_auto_20221112_1814"),
    ]

    operations = [
        migrations.CreateModel(
            name="Details",
            fields=[
                ("u_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("bp", models.CharField(max_length=30)),
                ("temp", models.CharField(max_length=30)),
                ("pulse", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(name="Table_D_BP",),
        migrations.DeleteModel(name="Table_OXY_S",),
        migrations.DeleteModel(name="Table_PR",),
        migrations.DeleteModel(name="Table_S_BP",),
        migrations.DeleteModel(name="Table_TEMP",),
    ]
