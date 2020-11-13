from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from .models import Question
from .forms import AddQuestionForm
from highScore.forms import AddUserAnswer

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


class QuestionView(View):

    def get(httprequest, *args):
        return render(httprequest, "home.html")

    def contact(httprequest, *args):
        return render(httprequest, "contact.html")

    @login_required
    def questionList(httprequest, *args, **kwargs):
        all_questions = Question.objects.all()
        dict_question = {
            "all_questions": all_questions,
        }
        return render(httprequest, "question_list.html", dict_question)

    @login_required
    def questionCreateView(httprequest, *args, **kwargs):
        add_question_form = AddQuestionForm(httprequest.POST or None, httprequest.FILES)

        if add_question_form.is_valid():
            add_question_form.save()
            add_question_form = AddQuestionForm()

        context = {
            "form": add_question_form
        }

        return render(httprequest, "question_create_view.html", context)

    @login_required
    def addQuestionResult(request, *args, **kwargs):
        correct_answer = []
        user_answer = request.POST

        if request.method != "POST":
            return render(request, "result.html")

        question_objects = Question.objects.values_list()

        for object in question_objects:
            correct_answer.append(object[len(object) - 1])

        userAnswerForm = AddUserAnswer(request.POST)
        userAnswerForm.is_valid()
        # newUserAnswerForm = userAnswerForm()
        # newUserAnswerForm.user.id = request.user.id
        # userAnswerForm.save()

        return render(request, "result.html")
