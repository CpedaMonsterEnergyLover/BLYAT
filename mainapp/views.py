from django.contrib.auth import logout, authenticate
from django.shortcuts import render, redirect

from mainapp.forms import RegisterForm



def exit_view(request):
    logout(request)
    return redirect('/home')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form = RegisterForm()
            return render(response, "registration/registration.html", {"form": form})

    form = RegisterForm()
    return render(response, "registration/registration.html", {"form": form})


def home(response):
    return render(response, "home.html")