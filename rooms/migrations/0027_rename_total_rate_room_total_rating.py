# Generated by Django 3.2 on 2021-07-04 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0026_room_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='total_rate',
            new_name='total_rating',
        ),
    ]
