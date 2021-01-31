# Generated by Django 3.1.3 on 2021-01-30 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egg_report', '0004_auto_20210129_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('position', models.CharField(choices=[('L', 'Kiri'), ('R', 'Kanan')], max_length=1)),
                ('is_empty', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='cage_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egg_report.cage', to_field='number'),
        ),
        migrations.DeleteModel(
            name='CageNum',
        ),
    ]