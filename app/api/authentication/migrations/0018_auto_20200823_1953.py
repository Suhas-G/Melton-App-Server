# Generated by Django 3.0.3 on 2020-08-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20200823_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
