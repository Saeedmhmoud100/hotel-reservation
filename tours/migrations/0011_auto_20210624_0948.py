# Generated by Django 3.2 on 2021-06-24 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_auto_20210624_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='data_from',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='data_to',
        ),
    ]
