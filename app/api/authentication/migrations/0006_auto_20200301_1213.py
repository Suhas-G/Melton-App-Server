# Generated by Django 3.0.3 on 2020-03-01 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0005_phonenumber_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="points",
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
