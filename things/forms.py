from django import forms
from .models import Thing, Review


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'nickname', 'description', 'website']

    def clean_name(self):
        data = self.cleaned_data['name']

        if data:
            # Capitalize first character.
            data = data[0].capitalize() + data[1:]

        return data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating', 'author']
