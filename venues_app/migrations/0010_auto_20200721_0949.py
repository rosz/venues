# Generated by Django 3.0.7 on 2020-07-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0009_auto_20200721_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
