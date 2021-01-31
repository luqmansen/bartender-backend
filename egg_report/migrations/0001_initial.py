# Generated by Django 3.1.3 on 2021-01-31 12:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('position', models.CharField(choices=[('L', 'Kiri'), ('R', 'Kanan')], max_length=1)),
                ('is_empty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_lay_egg', models.BooleanField(default=False)),
                ('cage_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egg_report.cage')),
            ],
        ),
    ]
