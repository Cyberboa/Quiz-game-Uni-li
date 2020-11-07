from django.db import models
from django.conf import settings


# Create your models here.
class HighScore(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    user_answer1 = models.TextField(default="")
    user_answer2 = models.TextField(default="")
    user_answer3 = models.TextField(default="")
    user_answer4 = models.TextField(default="")
    created_date = models.DateTimeField(null=True, editable=False, blank=True)

    def __str__(self):
        return str(self.player)
