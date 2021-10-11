from django.urls import path

from mainapp.views import cruise_list, liner_list, excursion_list, add_cruise, add_liner, add_excursion, edit_cruise, \
    edit_liner, edit_excursion, delete_cruise, delete_liner, delete_excursion, exit_view, register

urlpatterns = [
    path('exit', exit_view),
    path('accounts/register', register),

    path('cruise/list/', cruise_list),
    path('liner/list/', liner_list),
    path('excursion/list/', excursion_list),

    path('cruise/new/', add_cruise.as_view()),
    path('liner/new/', add_liner.as_view()),
    path('excursion/new/', add_excursion.as_view()),

    path('cruise/<int:pk>/update', edit_cruise.as_view()),
    path('liner/<int:pk>/update', edit_liner.as_view()),
    path('excursion/<int:pk>/update', edit_excursion.as_view()),

    path('cruise/<int:pk>/delete', delete_cruise.as_view()),
    path('liner/<int:pk>/delete', delete_liner.as_view()),
    path('excursion/<int:pk>/delete', delete_excursion.as_view()),
]