from django.urls import path

from mainapp.views import exit_view, register, home

urlpatterns = [
    path('exit', exit_view),
    path('accounts/register', register),

    path('home', home)
]