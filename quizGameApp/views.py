from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.
class HomeView(View):
    def get(httprequest, *args):
        my_dict = {
            "name": "roshan",
            "lastname": "hausammann",
            "year": 1922,
        }
        return render(httprequest, "home.html", my_dict)
