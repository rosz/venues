# Generated by Django 3.0.7 on 2020-07-21 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0012_auto_20200721_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='avg_rating',
        ),
    ]
