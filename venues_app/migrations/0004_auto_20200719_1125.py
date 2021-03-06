# Generated by Django 3.0.7 on 2020-07-19 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0003_auto_20200719_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='avg_rating',
            field=models.TextField(null=True, verbose_name='średnia ocen'),
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.TextField(null=True, verbose_name='obraz'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name='data dodania'),
        ),
    ]
