from django import forms
from .models import Question, Contact


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'question_image', 'option1', 'option2', 'option3', 'option4', 'correct_answer']


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'message']
