from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class HighScore(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True)
    user_answer1 = models.TextField(default="")
    user_answer2 = models.TextField(default="")
    user_answer3 = models.TextField(default="")
    user_answer4 = models.TextField(default="")
    created_date = models.DateTimeField(null=True, auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.player)
