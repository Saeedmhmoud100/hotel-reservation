# Generated by Django 3.2 on 2021-07-08 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last update'),
        ),
    ]
