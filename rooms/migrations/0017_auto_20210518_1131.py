# Generated by Django 3.2 on 2021-05-18 11:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0016_auto_20210518_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='data_from',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='data_to',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 5, 18, 11, 31, 28, 273862, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
