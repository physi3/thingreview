from django.test import TestCase
from django.utils import timezone

from .models import Thing, Review


class ThingModelTests(TestCase):
    def setUp(self):
        Thing.objects.create(
                name='Potato',
                description='A root vegetable first domesticated by native americans',
        )
    
    def test___str__(self):
        potato = Thing.objects.get(name='Potato')

        # Test: __str__ method
        self.assertEqual(str(potato), '<Thing name="Potato">')

    def test_get_rating(self):
        potato = Thing.objects.get(name='Potato')
        
        # Test: get_rating returns None if no child reviews
        self.assertIs(potato.get_rating(), None)

        # Test: get_rating returns average of child reviews (1 d.p)
        potato.review_set.create(name='a', content='a', rating=2)
        potato.review_set.create(name='b', content='b', rating=2.5)
        self.assertEqual(potato.get_rating(), 2.3)
