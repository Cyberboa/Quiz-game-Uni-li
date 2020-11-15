from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from .models import Question
from .forms import AddQuestionForm
from highScore.forms import AddUserAnswer


# Create your views here.
class QuestionView(View):

    def get(httprequest, *args):
        return render(httprequest, "home.html")

    def contact(httprequest, *args):
        return render(httprequest, "contact.html")

    def about(httprequest, *args):
        return render(httprequest, "about.html")

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
        correctAnswer = []
        userAnswer = {}
        score = 0
        question_objects = Question.objects.values_list()

        if request.method != "POST":
            return render(request, "result.html")

        for key, value in request.POST.items():
            if "csrfmiddlewaretoken" != key:
                userAnswer[key] = value

        for object in question_objects:
            correctAnswer.append(object[len(object) - 1])

        for key, value in userAnswer.items():
            if value in correctAnswer:
                score += 1

        player = request.user.id

        data = {'player': player, 'score': score, 'user_answer': userAnswer}

        completeForm = AddUserAnswer(data)

        if completeForm.is_valid():
            completeForm.save()

        return render(request, "result.html")
