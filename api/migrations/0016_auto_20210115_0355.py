# Generated by Django 3.1.3 on 2021-01-15 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210114_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='gallery_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='gallery_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='gallery_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/'),
        ),
    ]
