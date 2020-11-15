import itertools
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from .models import Question
from .forms import AddQuestionForm
from highScore.forms import AddUserAnswer


# Create your views here.
class QuestionView(View):
    """
    A class used to represent a Question

    ...

    Methods
    -------
    home()
        returns the home.html
    contact()
        returns the contact.html
    about()
        returns the about.html
    questionsList()
        Method is only available for login users
        returns the question_list.html and the dict_question
    questionCreateView()
        Method is only available for login users
        returns question_create_view.html
    addQuestionResult()
        Method is only available for login users
        returns the result.html
    """

    def home(httprequest, *args):
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
        """check add_question_form"""
        if add_question_form.is_valid():
            add_question_form.save()
            add_question_form = AddQuestionForm()

        context = {
            "form": add_question_form
        }

        return render(httprequest, "question_create_view.html", context)

    @login_required
    def addQuestionResult(request, *args, **kwargs):

        """Creating the needed variables"""
        correctAnswer = []
        questionsTemp = []
        userAnswer = {}
        temp_result = []
        dict_result = {"all_result": temp_result}
        player = request.user.id
        score = 0
        question_objects = Question.objects.values_list()

        """Adding the correct Answers in correctAnswer"""
        for object in question_objects:
            correctAnswer.append(object[len(object) - 1])
            temp_result.append({"question": object[len(object) - 7], "answer": "", "correct": object[len(object) - 1]})

        """If its not a POST then it will return result.html"""
        if request.method != "POST":
            return render(request, "result.html")

        """Adding the user answer into the dictionary"""
        index = 0
        for key, value in request.POST.items():

            """We dont want --> csrfmiddlewaretoken in the dictionary"""
            if "csrfmiddlewaretoken" != key:
                userAnswer[key] = value
                temp_result[index].update({"answer": value})
                index += 1

        """If the answer of the user is equal to the correct answer then the score will go up +1"""
        index = 0
        for key, value in userAnswer.items():
            if value in correctAnswer:
                temp_result[index].update({"correct": ''})
                score += 1
            index += 1

        """Creating the data for AddUserAnswer"""
        data = {'player': player, 'score': score, 'user_answer': userAnswer}

        """Creating the completeForm"""
        completeForm = AddUserAnswer(data)

        """Only save the form if it is valid"""
        if completeForm.is_valid():
            completeForm.save()

        return render(request, "result.html", dict_result)
