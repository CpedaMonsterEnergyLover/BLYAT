from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from mainapp.forms import RegisterForm
from mainapp.models import Cruise, Excursion, Liner


def exit_view(request):
    logout(request)
    return redirect('/liner/list')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/liner/list')
        else:
            form = RegisterForm()
            return render(response, "registration/registration.html", {"form": form})

    form = RegisterForm()
    return render(response, "registration/registration.html", {"form": form})


def cruise_list(request):
    access = False
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            access = True
    context = {"dataset": Cruise.objects.all(), "access": access}
    return render(request, 'cruise_list.html', context)


def liner_list(request):
    access = False
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            access = True
    context = {"dataset": Liner.objects.all(), "access": access}
    return render(request, 'liner_list.html', context)


def excursion_list(request):
    access = False
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            access = True
    context = {"dataset": Excursion.objects.all(), "access": access}
    return render(request, 'excursion_list.html', context)


class add_cruise(CreateView):
    model = Cruise
    template_name = 'add_cruise.html'
    success_url = 'http://127.0.0.1:8000/cruise/list'
    fields = ['name', 'days', 'length', 'stops']


class add_liner(CreateView):
    model = Liner
    template_name = 'add_liner.html'
    success_url = 'http://127.0.0.1:8000/liner/list'
    fields = ['name', 'number', 'team', 'tickets']


class add_excursion(CreateView):
    model = Excursion
    template_name = 'add_excursion.html'
    success_url = 'http://127.0.0.1:8000/excursion/list'
    fields = ['date', 'tickets', 'cruise', 'liner']


class edit_cruise(UpdateView):
    model = Cruise
    fields = ['name', 'days', 'length', 'stops']
    success_url = 'http://127.0.0.1:8000/cruise/list'
    template_name = 'edit_cruise.html'


class edit_liner(UpdateView):
    model = Liner
    fields = ['name', 'number', 'team', 'tickets']
    success_url = 'http://127.0.0.1:8000/liner/list'
    template_name = 'edit_liner.html'


class edit_excursion(UpdateView):
    model = Excursion
    fields = ['date', 'tickets', 'cruise', 'liner']
    success_url = 'http://127.0.0.1:8000/excursion/list'
    template_name = 'edit_excursion.html'


class delete_liner(DeleteView):
    model = Liner
    template_name = 'delete_object.html'
    success_url = "http://127.0.0.1:8000/liner/list"


class delete_cruise(DeleteView):
    model = Cruise
    template_name = 'delete_object.html'
    success_url = "http://127.0.0.1:8000/cruise/list"


class delete_excursion(DeleteView):
    model = Excursion
    template_name = 'delete_object.html'
    success_url = "http://127.0.0.1:8000/excursion/list"
