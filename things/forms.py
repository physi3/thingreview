from django import forms
from .models import Thing, Review


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'nickname', 'description', 'website']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating', 'author']
