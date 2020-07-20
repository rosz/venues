from django.conf import settings
from django.db import models
from django.utils import timezone


class RatingManager(models.Manager):
    def avg_rating(self):
        return Venue.objects.filter(venue=self.id).all().aggregate(models.Avg('price'))


class Venue(models.Model):
    name = models.CharField(max_length=100, verbose_name='nazwa')
    description = models.TextField(verbose_name='opis')
    address = models.TextField(verbose_name='adres')
    image = models.ImageField(verbose_name='obraz', upload_to='media', help_text="Dodaj obrazek o wymiarach 200x200px", null=True)
    avg_rating = models.TextField(verbose_name='średnia ocen', default=0)
    created_at = models.DateTimeField(verbose_name='data dodania', default=timezone.now)

    def __str__(self):
        return f'{self.name} @ {self.address}'

    def get_or_create(self):
        pass

    class Meta:
        verbose_name = 'Lokal'
        verbose_name_plural = 'Lokale'


# class User(models.Model):
#     def __str__(self):
#         return f'{self.username}'
#
#     class Meta:
#         verbose_name = 'Użytkownik'
#         verbose_name_plural = 'Użytkownicy'


class Rating(models.Model):
    RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    rate = models.IntegerField(choices=RATING, default='1')
    user = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, {self.venue}, {self.rate}'

    class Meta:
        unique_together = ['user', 'venue']
        verbose_name = 'Ocena użytkownika'
        verbose_name_plural = 'Oceny użytkowników'
