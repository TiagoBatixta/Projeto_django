# Generated by Django 4.2.11 on 2024-05-12 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("Nebulosa", "Nebulosa"),
                    ("Estrela", "Estrela"),
                    ("Galáxia", "Galáxia"),
                    ("Plaenta", "Plaenta"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
