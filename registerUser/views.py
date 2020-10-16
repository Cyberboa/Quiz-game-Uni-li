from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm


# Create your views here.
class Register(View):
    def registerUser(response, *args, **kwargs):
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                form.save()
            return redirect("/welcome/")

        else:
            form = RegisterForm()

        return render(response, "registerUser.html", {"form": form})
