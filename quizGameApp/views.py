from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


# Create your views here.
class HomeViewC(View):
    def get(self, *args):
        return HttpResponse("Hello World from the Class")
