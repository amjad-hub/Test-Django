# Generated by Django 3.0.8 on 2020-07-27 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_m',
            old_name='image_file',
            new_name='image',
        ),
    ]
