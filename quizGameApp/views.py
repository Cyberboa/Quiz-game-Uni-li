from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


# Create your views here.
class HomeView(View):
    def get(httprequest, *args):
        return render(httprequest, "home.html", {})
