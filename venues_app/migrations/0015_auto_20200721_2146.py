# Generated by Django 3.0.7 on 2020-07-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0014_auto_20200721_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(
                auto_now=True,
                verbose_name='data dodania'),
        ),
    ]
