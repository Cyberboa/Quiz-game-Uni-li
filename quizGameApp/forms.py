from django import forms

class AddQuestionForm(forms.Form):
    question = forms.CharField(max_length=100)
    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100)
    option4 = forms.CharField(max_length=100)
    corransw = forms.CharField(max_length=100)