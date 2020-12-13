from django.db import models


# Create your models here.

class Question(models.Model):
    """
        A class used to represent the datafield of Question

        ...

        Methods
        -------
        __str__(self)
            returns the question name
        """
    question = models.TextField()
    question_image = models.FileField(upload_to="questionImages/", blank=True, default='')
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_answer = models.TextField()

    def __str__(self):
        return self.question


# Create function submit button (Adi)
class Contact(models.Model):
    """
        A class used to represent the datafield of Contact

        ...

        Methods
        -------
        __str__(self)
            returns the firstname of the person
        """
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.firstname
