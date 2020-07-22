# Generated by Django 3.0 on 2020-07-18 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100,
                                           verbose_name='nazwa użytkownika')),
            ],
        ),
        migrations.RemoveField(
            model_name='venue',
            name='author',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='created_date',
        ),
        migrations.AddField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(
                2020, 7, 18, 13, 25, 36, 900562, tzinfo=utc), verbose_name='data dodania'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.TextField(verbose_name='adres'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='description',
            field=models.TextField(verbose_name='opis'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nazwa'),
        ),
    ]
