# Generated by Django 3.0.7 on 2020-07-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0019_auto_20200721_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='avg_rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
