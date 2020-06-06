from django import forms
from .models import *


class ComentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'rating')

    def clean_rating(self):
        cd = self.cleaned_data
        if cd['rating'] > 10 or cd['rating'] < 1:
            return forms.ValidationError("Рейтинг не может быть больше 10 или меньше 1")
        return cd['rating']