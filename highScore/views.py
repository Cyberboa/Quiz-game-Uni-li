from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from .models import HighScore


# Create your views here.
class Score(View):
    """
    A class which displays the view.

    ...

    Methods
    -------
    scoreList()
        returns the score.html & dict_score
    """

    @login_required
    def scoreList(httprequest, *args, **kwargs):
        ordered_all_scores = HighScore.objects.order_by('-score')
        dict_score = {
            "all_scores": ordered_all_scores,
        }
        return render(httprequest, "score.html", dict_score)
