# Generated by Django 4.2.2 on 2023-06-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_image_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='preview',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
