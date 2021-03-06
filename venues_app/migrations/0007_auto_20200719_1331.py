# Generated by Django 3.0.7 on 2020-07-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0006_auto_20200719_1212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={
                'verbose_name': 'Ocena użytkownika',
                'verbose_name_plural': 'Oceny użytkowników'},
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(
                default=0),
        ),
        migrations.AlterField(
            model_name='venue',
            name='avg_rating',
            field=models.TextField(
                default=0,
                verbose_name='średnia ocen'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(
                help_text='Dodaj obrazek o wymiarach 200x200px',
                null=True,
                upload_to='media',
                verbose_name='obraz'),
        ),
    ]
