# Django
from django.urls import path
from comparation import views

urlpatterns = [

    path(
        route='',
        view=views.home,
        name='home'
    ),

]
