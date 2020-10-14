from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Question


# Create your views here.
class HomeView(View):
    def get(httprequest, *args):
        my_dict = {
            "name": "roshan",
            "lastname": "hausammann",
            "year": 1922,
        }
        return render(httprequest, "home.html", my_dict)

    def questionList(httprequest, *args, **kwargs):
        allQuestions = Question.objects.all()
        context = {
            "allQuestions": allQuestions,
            "title": "My question list"
        }
        return render(httprequest, "question_list.html", context)
