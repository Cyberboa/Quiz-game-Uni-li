from django import forms
from .models import HighScore


class AddUserAnswer(forms.ModelForm):
    class Meta:
        model = HighScore
        fields = ['player', 'score', 'user_answer']
