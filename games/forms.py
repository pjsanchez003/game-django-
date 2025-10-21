
from django import forms
from .models import Game

class DateInput(forms.DateInput):
    input_type = "date"

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["title", "platform", "genre", "description", "release_date", "price", "cover"]
        widgets = {
            "release_date": DateInput(),
            "description": forms.Textarea(attrs={"rows": 4}),
        }
