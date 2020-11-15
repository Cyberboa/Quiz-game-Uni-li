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
- You also need to install crispy forms (easy layout)
    - pip install django-crispy-forms
- Create superuser for project members (each member needs to do it on his/her own)
    - python manage.py createsuperuser
- To compile scss to css you need to do the following:
    - pip install django-sass
- To use json in sqlite you need to download and edit the following file:
    - Instructions for Windows
    - Check your python installation - is it 32bit or 64bit? run: `python -c "import platform;print(platform.architecture()[0])"`
    - Download the [precompiled DLL](https://www.sqlite.org/download.html) that matches your Python installation (32-bit or 64-bit).
    - Locate your Python installation. By default, it should be in `%localappdata%\Programs\Python\PythonXX`, where XX is the Python version. For example, it's located in `C:\Users\<username>\AppData\Local\Programs\Python\Python37`. If you added Python installation directory to your PATH environment variable, you can run the command `where python` on a command prompt to locate it. Enter the DLLs directory in your Python installation.
    - Rename (or delete) `sqlite3.dll` inside the `DLLs` directory.
    - Extract `sqlite3.dll` from the downloaded DLL archive and put it in the `DLLs` directory.
    - Now, the JSON1 extension should be ready to be used in Python and Django.

## Execution for programming
- python manage.py runserver
- python manage.py sass quizGameApp/static/scss/ quizGameApp/static/css/ --watch