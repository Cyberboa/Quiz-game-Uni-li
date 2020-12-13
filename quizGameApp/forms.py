from django import forms
from .models import Question, Contact


class AddQuestionForm(forms.ModelForm):
    """
    A class used to input Questions into the database.

    """

    class Meta:
        model = Question
        fields = ['question', 'question_image', 'option1', 'option2', 'option3', 'option4', 'correct_answer']


class AddContactForm(forms.ModelForm):
    """
    A class used to input contact to the database.

    """

    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'message']
