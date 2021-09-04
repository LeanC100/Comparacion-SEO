# Django
from django.urls import path
from comparation import views

urlpatterns = [

    path(
        route='',
        view=views.Home,
        name='home'
    ),
    path(
        route='history/',
        view=views.HistoryView,
        name='history'
    ),
]
