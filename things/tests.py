from django.test import TestCase
from django.utils import timezone

from .models import Thing, Review


potato_description = 'A root vegetable first domesticated by native americans.'


class ThingModelTests(TestCase):
    potato = None
    def setUp(self):
        global potato
        potato = Thing.objects.create(
                name='Potato',
                description=potato_description,
        )
    
    def test___str__(self):
        global potato
        # Test: __str__ method
        self.assertEqual(str(potato), '<Thing name="Potato">')

    def test_get_rating(self):
        global potato
        # Test: get_rating returns None if no child reviews
        self.assertIs(potato.get_rating(), None)

        # Test: get_rating returns average of child reviews (1 d.p)
        potato.review_set.create(content='a', rating=2)
        potato.review_set.create(content='b', rating=2.5)
        self.assertEqual(potato.get_rating(), 2.3)


class ReviewModelTests(TestCase):
    potato = None
    def setUp(self):
        global potato
        potato = Thing.objects.create(
                name='Potato',
                description=potato_description,
        )
        potato.review_set.create(content='a', rating=2)
        potato.review_set.create(content='b', rating=2.5)

    def test___str__(self):
        global potato
        # Test: __str__ method
        a = potato.review_set.get(content='a')
        self.assertEqual(str(a), f'<Review thing="Potato"@{a.date}>')

    def test_save_rating(self):
        global potato
        # Test: rating after save method between 0-5 (inclusive)
        b = potato.review_set.get(content='b')
        b.rating = -1
        b.save()
        self.assertTrue(0 <= b.rating <= 5)
        
        b.rating = 6
        b.save()
        self.assertTrue(0 <= b.rating <= 5)

        # Test: parent thing rating average updates
        b.rating = 3
        b.save()
        self.assertEqual(potato.rating, 2.5)
