from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class Score(View):
    @login_required
    def get(httprequest, *args):
        return render(httprequest, "score.html")
