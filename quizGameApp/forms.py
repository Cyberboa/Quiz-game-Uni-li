from django import forms
from .models import Question


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']
