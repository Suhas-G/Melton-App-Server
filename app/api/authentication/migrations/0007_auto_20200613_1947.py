# Generated by Django 3.0.3 on 2020-06-13 14:17

import authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20200301_1213'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', authentication.models.AppUserManager()),
            ],
        ),
    ]
