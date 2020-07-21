from django.db import models
from django.utils import timezone


class RatingManager(models.Manager):
    def avg_rating(self):
        avg = Venue.objects.filter(id=self.id).aggregate(
            avg=models.Avg('rating__rate')).get("avg")
        if avg is None:
            return "Jeszcze nikt nie ocenił."
        return round(avg, 1)


class Venue(models.Model):
    name = models.CharField(max_length=100, verbose_name='nazwa')
    description = models.TextField(verbose_name='opis')
    address = models.CharField(max_length=255, verbose_name='adres')
    image = models.ImageField(
        verbose_name='obraz',
        upload_to='media',
        help_text="Dodaj obrazek o wymiarach 200x200px",
        null=True)
    avg_rating = RatingManager.avg_rating
    created_at = models.DateTimeField(
        verbose_name='data dodania', default=timezone.now)

    def __str__(self):
        return f'{self.name} @ {self.address}'

    class Meta:
        verbose_name = 'Lokal'
        verbose_name_plural = 'Lokale'


class Rating(models.Model):
    RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    rate = models.IntegerField(choices=RATING, default=5)
    user = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, {self.venue}, {self.rate}'

    class Meta:
        unique_together = ['user', 'venue']
        verbose_name = 'Ocena użytkownika'
        verbose_name_plural = 'Oceny użytkowników'
