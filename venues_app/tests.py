from django.contrib.auth.models import User
from django.test import TestCase, Client
from venues_app.models import Venue, Rating


class TestRating(TestCase):
    rates = (1, 3, 5)

    def test_avg_rating(self):
        test_restaurant = Venue.objects.create(
            name='Test Restaurant 1', description="test description")
        test_user_1 = User.objects.create_user(username="Test Name 1")
        test_user_2 = User.objects.create_user(username="Test Name 2")
        test_user_3 = User.objects.create_user(username="Test Name 3")

        Rating.objects.create(
            rate=self.rates[0], venue=test_restaurant, user=test_user_1)
        Rating.objects.create(
            rate=self.rates[1], venue=test_restaurant, user=test_user_2)
        Rating.objects.create(
            rate=self.rates[2], venue=test_restaurant, user=test_user_3)

        expected = Venue.objects.filter(id=test_restaurant.id).first()
        self.assertEqual(expected.avg_rating, round(
            sum(self.rates) / len(self.rates), 1))

    def test_rating_request(self):
        rate_1st = 3
        rate_2nd = 5
        test_restaurant = Venue.objects.create(
            name='Test Restaurant 1', description="test description")
        test_user = User.objects.create_user(username="Test Name 1")
        # test_rating = Rating.objects.create(
        #     rate=rate_1st, venue=test_restaurant, user=test_user)

        response = self.client.post(path=f'/venue/{test_restaurant.id}/rate')
        self.assertEqual(response.status_code, 200)


class TestFetching(TestCase):
    client = Client()

    def test_venue_fetching(self):
        test_restaurant = Venue.objects.create(
            name='Test Restaurant 1',
            description="test description",
            image='media/',
            address='Test Address'
        )
        response = self.client.post(path=f'/venue/{test_restaurant.id}')
        self.assertEqual(response.status_code, 200)

        unexisting_id = 10
        response = self.client.post(path=f'/venue/{unexisting_id}')
        self.assertEqual(response.status_code, 404)


class TestUserAuth(TestCase):
    client = Client()

    def test_register(self):
        pass

    def test_login(self):
        pass

    def test_logout(self):
        pass
