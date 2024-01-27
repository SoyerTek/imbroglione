from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.newgame, name="newgame"),
    path("<int:game_id>/", views.play, name="play"),
]