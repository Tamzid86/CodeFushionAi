# Generated by Django 4.2.20 on 2025-05-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country_code", models.CharField(max_length=10)),
                ("country_name", models.CharField(max_length=255)),
                ("full_data", models.JSONField()),
            ],
        ),
    ]
