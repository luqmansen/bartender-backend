# Generated by Django 3.1.3 on 2021-01-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201221_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='gallery_image_1',
            field=models.ImageField(null=True, upload_to='images/content/'),
        ),
        migrations.AddField(
            model_name='content',
            name='gallery_image_2',
            field=models.ImageField(null=True, upload_to='images/content/'),
        ),
        migrations.AddField(
            model_name='content',
            name='gallery_image_3',
            field=models.ImageField(null=True, upload_to='images/content/'),
        ),
    ]
