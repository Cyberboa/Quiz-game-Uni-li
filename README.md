# ISD Project Quiz-game-Uni-li
 For our 1 semester we want to do a Quiz game.<br>
 All topics which we had in our 1 semester will be asked in the game. <br>
 The following functions will be implemented: <br>
 Highscore, Help function, Instruction manual, quiz question with 4 choices.<br>
 
## Installation
- Installation of your virtual environment
    - python -m venv venv
- How to activate your virtual environment
    - venv\Scripts\activate.bat
- You need to install django in your virtual environment
    - pip install django
- You also need to install crispy forms (easy layouting)
    - pip install django-crispy-forms
- Create superuser for project members
    - python manage.py createsuperuser
- To compile scss to css you need to do the following:
    - pip install django-sass

## Execution
- python manage.py runserver
- python manage.py sass quizGameApp/static/scss/ quizGameApp/static/css/ --watch