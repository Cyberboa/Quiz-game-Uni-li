from django import forms
from .models import HighScore


class AddUserAnswer(forms.ModelForm):
    class Meta:
        model = HighScore
        fields = ['user_answer1', 'user_answer2', 'user_answer3', 'user_answer4']