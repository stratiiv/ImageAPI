# Generated by Django 4.2.2 on 2023-06-11 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_type',
        ),
    ]
