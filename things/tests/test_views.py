from django.test import Client
from django.test import TestCase
from django.urls import reverse


class RandomViewTests(TestCase):
    def test_redirect_on_empty_thing_table(self):
        client = Client()
        res = client.get(reverse('things:random'))
        self.assertEqual(res.status_code, 302)


class LatestViewTests(TestCase):
    def test_redirect_on_empty_thing_table(self):
        client = Client()
        res = client.get(reverse('things:latest'))
        self.assertEqual(res.status_code, 302)


class LeastReviewedViewTest(TestCase):
    def test_redirect_on_empty_thing_table(self):
        client = Client()
        res = client.get(reverse('things:least_reviewed'))
        self.assertEqual(res.status_code, 302)
