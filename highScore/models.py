from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class HighScore(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True)
    user_answer = models.JSONField(default=list)
    created_date = models.DateTimeField(null=True, auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.player)
