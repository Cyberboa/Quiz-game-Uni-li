from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from .models import HighScore


# Create your views here.
class Score(View):
    @login_required
    def scoreList(httprequest, *args, **kwargs):
        all_scores = HighScore.objects.all()
        dict_score = {
            "all_scores": all_scores,
        }
        return render(httprequest, "score.html", dict_score)
