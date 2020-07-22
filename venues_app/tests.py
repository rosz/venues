from django.contrib.auth.models import User
from django.test import TestCase, Client
from venues_app.models import Venue, Rating


class TestRating(TestCase):
    rates = (1, 3, 5)

    def setUp(self):
        self.client = Client()
        self.restaurant = Venue.objects.create(
            name='Test Restaurant 1', description='test description')
        self.user_1st = User.objects.create_user(
            username='Test Name 1', password='testpassword123')
        self.user_2st = User.objects.create_user(
            username='Test Name 2', password='testpassword123')
        self.user_3st = User.objects.create_user(
            username='Test Name 3', password='testpassword123')

    def test_avg_rating(self):
        test_restaurant = Venue.objects.create(
            name='Test Restaurant 1', description='test description')

        Rating.objects.create(
            rate=self.rates[0], venue=test_restaurant, user=self.user_1st)
        Rating.objects.create(
            rate=self.rates[1], venue=test_restaurant, user=self.user_2st)
        Rating.objects.create(
            rate=self.rates[2], venue=test_restaurant, user=self.user_3st)

        expected = Venue.objects.filter(id=test_restaurant.id).first()
        self.assertEqual(expected.avg_rating, round(
            sum(self.rates) / len(self.rates), 1))

    def test_rating_request(self):
        rating_1st = 5
        rating_2nd = 3

        self.client.login(username='Test Name 1', password='testpassword123')
        self.client.post(
            path=f'/venue/{self.restaurant.id}/rate',
            data={
                'rate': rating_1st})
        rating_from_db = Rating.objects.filter(
            venue=self.restaurant).first().rate
        self.assertEqual(rating_from_db, rating_1st)

        # override rating for the same restaurant
        self.client.post(
            path=f'/venue/{self.restaurant.id}/rate',
            data={
                'rate': rating_2nd})
        rating_from_db = Rating.objects.filter(
            venue=self.restaurant).first().rate
        self.assertEqual(rating_from_db, rating_2nd)


class TestFetching(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Venue.objects.create(
            name='Fancy Test Name',
            description='test description',
            image='media/',
            address='Test Address'
        )
        self.user = User.objects.create_user(
            username='Test Name 1', password='testpassword123')

    def test_venue_fetching(self):
        response = self.client.post(path=f'/venue/{self.restaurant.id}')
        self.assertEqual(response.status_code, 200)

        unexisting_id = 10
        response = self.client.post(path=f'/venue/{unexisting_id}')
        self.assertEqual(response.status_code, 404)

    def test_search(self):
        response = self.client.get(path=f'/search',
                                   data={'search_name': self.restaurant.name[11:]})
        self.assertContains(
            response=response,
            text=self.restaurant.name,
            status_code=200)

        response = self.client.get(
            path=f'/search', data={'search_name': self.restaurant.name[7:10]})
        self.assertContains(
            response=response,
            text=self.restaurant.name,
            status_code=200)

        response = self.client.get(path=f'/search',
                                   data={'search_name': self.restaurant.name[:5]})
        self.assertContains(
            response=response,
            text=self.restaurant.name,
            status_code=200)

        response = self.client.get(path=f'/search',
                                   data={'search_name': 'unextisting name'})
        self.assertNotContains(
            response=response,
            text=self.restaurant.name,
            status_code=200)
