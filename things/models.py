from django.db import models
from django.utils.translation import gettext_lazy as _

from decimal import Decimal, ROUND_HALF_UP

class Thing(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    website = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
    )

    def get_rating(self):
        if self.review_set.count() == 0:
            return None
        ratings = [r.rating for r in self.review_set.all()]
        return Decimal(sum(ratings) / len(ratings)).quantize(Decimal('0.0'), ROUND_HALF_UP)

    def __repr__(self):
        return f'<Thing name="{self.name}">'
    __str__ = __repr__


class Review(models.Model):
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    author = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'<Review thing="{self.thing.name}"@{self.date}>'
    __str__ = __repr__

    def save(self, *args, **kwargs):
        # Keep rating between 0 and 5.
        if self.rating > 5:
            self.rating = 5
        elif self.rating  < 0:
            self.rating = 0

        super().save(*args, **kwargs)

        # Update the average rating in parent.
        ratings = [r.rating for r in self.thing.review_set.all()]
        rating = round(sum(ratings) / len(ratings), 2)
        self.thing.rating = rating
        self.thing.save()
