from django import forms

from venues_app.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rate',)
