from django import forms

from venues_app.models import Rating


class RatingForm(forms.ModelForm):
    rate = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self.rate = kwargs.pop('rate', None)
        super(RatingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rating
        fields = ('rate',)
