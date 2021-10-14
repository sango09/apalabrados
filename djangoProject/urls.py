# Django
from django.urls import path

# Views
from apalabrados import views

urlpatterns = [
    path(
        route='',
        view=views.InputView.as_view(),
        name='index'
    ),
    path(
        route='data/',
        view=views.DataListView.as_view(),
        name='list'
    ),
]
