# Generated by Django 3.1.3 on 2021-01-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210114_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='fun_fact',
            field=models.TextField(default=None),
        ),
    ]