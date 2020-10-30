from django.db import models
from django.conf import settings


# Create your models here.

class HighScore(models.Model):
    # player = models.ForeignKey(settings.AUTH_USER_MODEL)
    score = models.SmallIntegerField()

    def __str__(self):
        return self.question
