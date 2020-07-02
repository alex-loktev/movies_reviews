from django.test import TestCase
from main.models import *


class UrlTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title="brabra",
            slug="brabra"
        )
        self.film = Film.objects.create(
            title="blabla",
            slug="blabla",
            description="blabla",
            release="2000-03-19",
            image="NULL",
            rating=10
        )

    def tearDown(self):
        self.category.delete()
        self.film.delete()

    def test_home(self):
        response = self.client.get('/main/home/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get('/main/category/{}'.format(self.category.slug))
        self.assertEqual(response.status_code, 200)