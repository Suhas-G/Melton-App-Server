# Generated by Django 3.0.3 on 2020-07-11 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0015_auto_20200711_1559"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SustainableDevelopmentGoals",
            new_name="SustainableDevelopmentGoal",
        ),
    ]
