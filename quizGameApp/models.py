from django.db import models


# Create your models here.

class Question(models.Model):
    question = models.TextField()
    question_image = models.FileField(upload_to="questionImages/", blank=True, default='')
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_answer = models.TextField()

    def __str__(self):
        return self.question
