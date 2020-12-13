from django import forms
from .models import HighScore


class AddUserAnswer(forms.ModelForm):
    """
    A class used to input data to the database.

    """

    class Meta:
        model = HighScore
        fields = ['player', 'score', 'user_answer']
