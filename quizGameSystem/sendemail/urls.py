#Diese ganze Seite wurde von Adrian erstellt für das Kontaktformular

(contact) $ touch sendemail/urls.py

# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path('contact/', contactView, name='contact'), # Adrian_contactUs_page
    path('success/', successView, name='success'), # Adrian_contactUs_page
]
