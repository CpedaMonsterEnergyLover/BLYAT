from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from mainapp.forms import RegisterForm
from mainapp.models import Cruise, Excursion, Liner


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