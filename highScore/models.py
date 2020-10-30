from django.db import models
from django.conf import settings


# Create your models here.

class HighScore(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.SmallIntegerField()

    def __str__(self):
        return str(self.player)
