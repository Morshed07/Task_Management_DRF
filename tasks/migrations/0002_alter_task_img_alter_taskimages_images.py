# Generated by Django 5.0.1 on 2024-01-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='taskimages',
            name='images',
            field=models.ImageField(blank=True, default='', null=True, upload_to='task_images'),
        ),
    ]
