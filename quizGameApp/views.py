from django.shortcuts import render
from django.views.generic import View
from .models import Question
from .forms import AddQuestionForm

# Create your views here.
"""
A class used to represent a question

...

Attributes
----------
my_dict : dict of str : str and int
all_questions : QuerySet
context : dict of all_questions and title
my_form : AddQuestionForm to add a question to the DB

Methods
-------

"""


class HomeView(View):
    def get(httprequest, *args):
        my_dict = {
            "name": "roshan",
            "lastname": "hausammann",
            "year": 1922,
        }
        return render(httprequest, "home.html", my_dict)

    def questionList(httprequest, *args, **kwargs):
        all_questions = Question.objects.all()
        dict_question = {
            "all_questions": all_questions,
            "title": "Quiz Game Uni Liechtenstein"
        }
        return render(httprequest, "question_list.html", dict_question)

    def questionCreateView(httprequest, *args, **kwargs):
        my_form = AddQuestionForm(httprequest.POST or None)
        if my_form.is_valid():
            my_form.save()
            my_form = AddQuestionForm()

        context = {
            "form": my_form
        }
        return render(httprequest, "question_create_view.html", context)
