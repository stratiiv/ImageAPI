# Generated by Django 4.2.2 on 2023-06-11 10:05

from django.db import migrations, models
import images.services


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_image_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images', validators=[images.services.validate_image]),
        ),
    ]
