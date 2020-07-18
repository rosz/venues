from django.db import models
from django.utils import timezone


class Venue(models.Model):
    name = models.CharField(max_length=100, verbose_name='nazwa')
    description = models.TextField(verbose_name='opis')
    address = models.TextField(verbose_name='adres')
    # image = models.ImageField()
    avg_rating = models.Aggregate()
    created_at = models.DateTimeField(verbose_name='data dodania', default=timezone.now())

    def __str__(self):
        return f'{self.name} @ {self.address}'

    def add(self):
        self.save()

    class Meta:
        verbose_name = 'Lokal'
        verbose_name_plural = 'Lokale'


class User(models.Model):
    login = models.CharField(max_length=100, verbose_name='nazwa użytkownika')

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'


class Rating(models.Model):
    rate = models.IntegerChoices
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    venue = models.ForeignKey(to=Venue, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ['user', 'venue']
        verbose_name = 'Ocena'
        verbose_name_plural = 'Oceny'
